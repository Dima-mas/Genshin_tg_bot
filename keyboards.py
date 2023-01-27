from aiogram import types

start_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Старт',callback_data='Далее'))

gender_choice = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Люмин',callback_data='female'),
                                                 types.InlineKeyboardButton('Итер',callback_data='male'))

cool_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Круто!',callback_data='Круто!'))

backup_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('В главное меню',callback_data='Меню'))

main_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Выбор баннера',callback_data='banner_choice'),
                                                 types.InlineKeyboardButton('Галерея',callback_data='gallery'))

banner_choice_keyboard = types.InlineKeyboardMarkup(row_width=2).add(types.InlineKeyboardButton('Архонты',callback_data='archons'),
                                                          types.InlineKeyboardButton('Адепты',callback_data='adepti'),
                                                          types.InlineKeyboardButton('Мондштадт',callback_data='mondstadt'),
                                                          types.InlineKeyboardButton('Ли Юэ',callback_data='liyue'),
                                                          types.InlineKeyboardButton('Инадзума',callback_data='inazuma'),
                                                          types.InlineKeyboardButton('Сумеру',callback_data='sumeru'))

banner_choice_keyboard.row(types.InlineKeyboardButton('В главное меню',callback_data='Меню'))


banner_keyboard = {'archons':types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton('Молитва',callback_data='archons'),
                                                    types.InlineKeyboardButton('Список персонажей',callback_data='archons_char'),
                                                    types.InlineKeyboardButton('Назад к выбору баннера',callback_data='banner_choice')),
                   
                   'adepti':types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton('Молитва',callback_data='adepti'),
                                                    types.InlineKeyboardButton('Список персонажей',callback_data='adepti_char'),
                                                    types.InlineKeyboardButton('Назад к выбору баннера',callback_data='banner_choice')),
                   
                   'mondstadt':types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton('Молитва',callback_data='mondstadt'),
                                                    types.InlineKeyboardButton('Список персонажей',callback_data='mondstadt_char'),
                                                    types.InlineKeyboardButton('Назад к выбору баннера',callback_data='banner_choice')),
                   
                   'liyue':types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton('Молитва',callback_data='liyue'),
                                                    types.InlineKeyboardButton('Список персонажей',callback_data='liyue_char'),
                                                    types.InlineKeyboardButton('Назад к выбору баннера',callback_data='banner_choice')),
                   
                   'inazuma':types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton('Молитва',callback_data='inazuma'),
                                                    types.InlineKeyboardButton('Список персонажей',callback_data='inazuma_char'),
                                                    types.InlineKeyboardButton('Назад к выбору баннера',callback_data='banner_choice')),
                   
                   'sumeru':types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton('Молитва',callback_data='sumeru'),
                                                    types.InlineKeyboardButton('Список персонажей',callback_data='sumeru_char'),
                                                    types.InlineKeyboardButton('Назад к выбору баннера(2 клика)',callback_data='banner_choice'))
}







# adepti_keyboard = 
# mondstadt_keyboard = 
# liyue_keyboard = 
# inazuma_keyboard = 
# sumeru_keyboard = 
