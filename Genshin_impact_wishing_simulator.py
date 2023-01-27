import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from keyboards import *
from functions import *
from decouple import config


api_token = config('APIKEY')
API_TOKEN = api_token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class Form_beginning(StatesGroup):
    first_character_state = State()
    gender_choice_state = State()
    info_state = State()



class Form_wishing(StatesGroup):
    main_menu_state = State()
    main_choice_state = State()
    gallery_state = State()
    banner_choice_state = State()
    roll_or_nah_state = State()



@dp.message_handler(commands=['start'],state='*')
async def start(message: types.Message,state:FSMContext):
        await message.answer(text['starting'],reply_markup=start_keyboard)
        await Form_beginning.first_character_state.set()
        await state.update_data(roll_or_nah_state=0)

 
@dp.callback_query_handler(state=Form_beginning.first_character_state)
async def first_character_choice(query: types.CallbackQuery,state:FSMContext):
        if not load_gallery() == 'Галерея пока-что пуста ¯\_(ツ)_/¯':
                await query.message.edit_text('Похоже, что ты уже выбрал своего первого персонажа.\nТогда переносим тебя на главное меню',reply_markup=backup_keyboard)
                await Form_wishing.main_menu_state.set()
        else:
                await query.message.delete()
                await query.message.answer_photo('https://static.wikia.nocookie.net/gensin-impact/images/2/29/Traveler_Card.png/revision/latest?cb=20220725205258',text['first_character_choice'],reply_markup=gender_choice)
                await Form_beginning.gender_choice_state.set()


@dp.callback_query_handler(state=Form_beginning.gender_choice_state)
async def first_character_yay(query: types.CallbackQuery,state:FSMContext):
        start_character = (data['start_character'][query.data])
        add_to_gallery(start_character)
        await query.message.delete()
        await query.message.answer_photo(text[query.data][1],text[query.data][0],reply_markup=cool_keyboard)
        await Form_beginning.info_state.set()


@dp.callback_query_handler(state=Form_beginning.info_state)
async def basic_information(query: types.CallbackQuery,state:FSMContext):
        await query.message.delete()
        await query.message.answer(text['info'],reply_markup=backup_keyboard)
        await Form_wishing.main_menu_state.set()







@dp.callback_query_handler(state=Form_wishing.main_choice_state)
async def main_choice(query: types.CallbackQuery,state:FSMContext):
        if query.data == 'banner_choice':
                await query.message.delete()
                await query.message.answer('Какой баннер тебе нужен?',reply_markup=banner_choice_keyboard)
                await Form_wishing.banner_choice_state.set()
        elif query.data == 'gallery':
                loaded_gallery = load_gallery() 
                await query.message.edit_text(loaded_gallery,reply_markup=backup_keyboard)
                await Form_wishing.main_menu_state.set()


@dp.callback_query_handler(state=Form_wishing.banner_choice_state)
async def banner_choice(query: types.CallbackQuery,state:FSMContext):
        if query.data != 'Меню':
                await query.message.delete()
                await query.message.answer_photo(banner_info[query.data][1],banner_info[query.data][0],reply_markup=banner_keyboard[query.data])
                await Form_wishing.roll_or_nah_state.set()
        else:
                await query.message.edit_text('Главное меню',reply_markup=main_keyboard)
                await Form_wishing.main_choice_state.set()


@dp.callback_query_handler(state=Form_wishing.roll_or_nah_state)
async def roll_or_back(query: types.CallbackQuery,state:FSMContext):
        if '_char' in query.data:
                await query.message.delete()
                await query.message.answer(f'Персонажи, которых можно получить в этом баннере:{banner_details[query.data]}',reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Назад',callback_data=query.data[0:-5])))
                await Form_wishing.banner_choice_state.set()
        elif query.data == 'banner_choice':
                await Form_wishing.main_choice_state.set()
                await query.message.delete()
                await query.message.answer('Нажми ещё раз для перехода',reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Назад к выбору баннера',callback_data='banner_choice')))
        else:
                async with state.proxy() as state_info:
                        await state.update_data(roll_or_nah_state=state_info['roll_or_nah_state']+1)
                        rolled_character = roll(query.data,state_info['roll_or_nah_state'])
                        backwards_button = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Назад',callback_data=query.data))
                        if state_info['roll_or_nah_state'] > 7:
                                await state.update_data(roll_or_nah_state=0)
                                animation = await bot.send_animation(query.message.chat.id,'https://tenor.com/ru/view/genshin-impact-pull-wish-5star-five-star-gif-25193765')
                        else:
                                animation = await bot.send_animation(query.message.chat.id,'https://tenor.com/ru/view/genshin-impact-animation-wish-four-star-4star-gif-25193696')
                        await query.message.delete()
                        animation
                        await asyncio.sleep(5)
                        await bot.delete_message(query.message.chat.id,animation['message_id'])
                        
                        if rolled_character[0] != '\nУвы, 4-звёздночных архонтов пока не существует :(':
                                if not is_in_gallery(rolled_character[0]):
                                        result = query.message.answer_photo(rolled_character[1],f'Ты получил:\n{rolled_character[0]}(Новый!)',reply_markup=backwards_button)
                                        add_to_gallery(rolled_character[0])
                                else:
                                        result = query.message.answer_photo(rolled_character[1],f'Ты получил:\n{rolled_character[0]}(Копия)',reply_markup=backwards_button)
                        else:
                                result = query.message.answer_photo(rolled_character[1],rolled_character[0],reply_markup=backwards_button)
                await result
                await Form_wishing.banner_choice_state.set()


@dp.callback_query_handler(state='*')
async def main_menu(query: types.CallbackQuery,state:FSMContext):
        if query.data == 'Меню':
                await query.message.delete()
                await query.message.answer('Главное меню',reply_markup=main_keyboard)
                await Form_wishing.main_choice_state.set()


@dp.message_handler(state='*')
async def you_lost(message: types.Message,state: FSMContext):
        await message.answer('Похоже, ты потерялся.\nИспользуй команду /start, чтобы вернуться в начало бота')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)