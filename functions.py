import json
from random import randint as ran

text_data =  {'banner_drops':{
    'archons':{'5-star':('venti','zhongli','raiden','nahida'),'4-star':('no 4-star archons yet','no 4-star archons yet')},
    'adepti':{'5-star':('qiqi','albedo','ganyu','shenhe','xiao'),'4-star':('yanfei','yanfei')},
    'mondstadt':{'5-star':('eula','klee','mona','jean','diluc'),'4-star':('diona','fischl','rosaria','sucrose','razor','amber','kaeya','lisa','barbara','bennett','noelle')},
    'liyue':{'5-star':('keqing','hu-tao','tartaglia','yelan'),'4-star':('yaoyao','chongyun','beidou','xinyan','ningguang','xiangling','xingqiu','yun-jin')},
    'inazuma':{'5-star':('arataki-itto','ayaka','ayato','kazuha','kokomi','yae-miko','yoimiya'),'4-star':('kuki-shinobu','sara','thoma','gorou','shikanoin-heizou','sayu')},
    'sumeru':{'5-star':('tighnari','cyno','nilou','wanderer'),'4-star':('collei','candace','dori','faruzan','layla')}},
         'banner_info':{'mondstadt':('Мондштадт - это город-государство, который поклоняется Анемо Архонту Барбатосу.\nИдеал Архонта Мондштадта - свобода','https://static.wikia.nocookie.net/genshin-impact/images/2/20/%D0%9C%D0%BE%D0%BD%D0%B4%D1%88%D1%82%D0%B0%D0%B4%D1%82.jpg/revision/latest/scale-to-width-down/1000?cb=20210623202430&path-prefix=ru'),
                       'liyue':('Ли Юэ - это страна, в которой поклоняются Гео Архонту Мораксу или же Властелину Камня, как его называют сами жители.\nИдеал Архонта Ли Юэ - контракты','https://static.wikia.nocookie.net/gensin-impact/images/0/03/Liyue.png/revision/latest/scale-to-width-down/1000?cb=20221123013534'),
                       'inazuma':('Инадзума - это страна, которая поклоняется Электро Архонту, Райдэн Эи.\nИдеал Архонта Инадзумы - вечность','https://static.wikia.nocookie.net/genshin-impact/images/e/eb/%D0%A2%D1%8D%D0%BD%D1%81%D1%8E%D0%BA%D0%B0%D0%BA%D1%83.png/revision/latest?cb=20220118191809&path-prefix=ru'),
                       'sumeru':('Сумеру - это страна, в которой поклоняются Богине Мудрости, Дендро Архонту малой властительнице Кусанали.\n Идеал Архонта Сумеру - мудрость','https://cdn2.unrealengine.com/image-1-3840x2160-6fb63d0b460b.jpg'),
                       'archons':('Архонты — боги, правящие своими регионами в Тейвате. Каждый Архонт связан со своим элементом и идеалом.\nАрхонты могут даровать людям с особенно сильной волей знак своего уважения - Глаз Бога','https://castlepeak.ru/castlecellar/uploads/Arhonty.jpg'),
                       'adepti':('Адепты - группа магических существ, сосредоточенных в Ли Юэ. Они подчиняются контракту, составленному Мораксом, оберегая регион от демонических сил и злых божеств','https://static.wikia.nocookie.net/gensin-impact/images/d/de/Yakshas_-_Trailer.png/revision/latest/scale-to-width-down/1000?cb=20210127214939')},
         'banner_details':{'archons_char':'\nСёгун Райдэн (⭐⭐⭐⭐⭐) ⚡\nВенти (⭐⭐⭐⭐⭐) 💨\nЧжун Ли (⭐⭐⭐⭐⭐) 🗿\nНахида (⭐⭐⭐⭐⭐) 🌱',
                         'adepti_char':'\nЦи Ци (⭐⭐⭐⭐⭐) ❄\nАльбедо (⭐⭐⭐⭐⭐) 🗿\nГань Юй (⭐⭐⭐⭐⭐) ❄\nШэнь Хэ (⭐⭐⭐⭐⭐) ❄\nСяо (⭐⭐⭐⭐⭐) 💨\nЯнь Фэй (⭐⭐⭐⭐) 🔥',
                         'mondstadt_char':'\nДилюк (⭐⭐⭐⭐⭐) 🔥\nЭола (⭐⭐⭐⭐⭐) ❄\nДжинн (⭐⭐⭐⭐⭐) 💨\nКли (⭐⭐⭐⭐⭐) 🔥\nМона (⭐⭐⭐⭐⭐) 💧\nНоэлль (⭐⭐⭐⭐) 🗿\nРэйзор (⭐⭐⭐⭐) ⚡\nФишль (⭐⭐⭐⭐) ⚡\nАмбер (⭐⭐⭐⭐) 🔥\nКэйа (⭐⭐⭐⭐) ❄\nЛиза (⭐⭐⭐⭐) ⚡\nБарбара (⭐⭐⭐⭐) 💧\nБеннет (⭐⭐⭐⭐) 🔥\nДиона (⭐⭐⭐⭐) ❄\nРозария (⭐⭐⭐⭐) ❄\nСахароза (⭐⭐⭐⭐) 💨',
                         'liyue_char':'\nКэ Цин (⭐⭐⭐⭐⭐) ⚡\nХу Тао (⭐⭐⭐⭐⭐) 🔥\nТарталья (⭐⭐⭐⭐⭐) 💧\nЕ Лань (⭐⭐⭐⭐⭐) 💧\nЮнь Цзинь (⭐⭐⭐⭐) 🗿\nСин Цю (⭐⭐⭐⭐) 💧\nСян Лин (⭐⭐⭐⭐) 🔥\nНин Гуан (⭐⭐⭐⭐) 🗿\nСинь Янь (⭐⭐⭐⭐) 🔥\nЧун Юнь (⭐⭐⭐⭐) ❄\nБэй Доу (⭐⭐⭐⭐) ⚡',
                         'inazuma_char':'\nАратаки Итто (⭐⭐⭐⭐⭐) 🗿\nКамисато Аяка (⭐⭐⭐⭐⭐) ❄\nКамисато Аято (⭐⭐⭐⭐⭐) 💧\nКадзуха (⭐⭐⭐⭐⭐) 💨\nКокоми (⭐⭐⭐⭐⭐) 💧\nЯэ Мико (⭐⭐⭐⭐⭐) ⚡\nЁимия (⭐⭐⭐⭐⭐) 🔥\nТома (⭐⭐⭐⭐) 🔥\nХейдзо (⭐⭐⭐⭐) 💨\nГоро (⭐⭐⭐⭐) 🗿\nКуки Синобу (⭐⭐⭐⭐) ⚡\nСаю (⭐⭐⭐⭐) 💨\nСара (⭐⭐⭐⭐) ⚡',
                         'sumeru_char':'\nТигнари (⭐⭐⭐⭐⭐) 🌱\nСтранник(⭐⭐⭐⭐⭐) 💨\nНилу (⭐⭐⭐⭐⭐) 💧\nСайно (⭐⭐⭐⭐⭐) ⚡\nКоллеи (⭐⭐⭐⭐) 🌱\nЛайла (⭐⭐⭐⭐) ❄\nФарузан (⭐⭐⭐⭐) 💨\nДори (⭐⭐⭐⭐) ⚡\nКандакия (⭐⭐⭐⭐) 💧'},
         'start_character':{'female':'Люмин (⭐⭐⭐⭐⭐) 💨🗿⚡🌱','male':'Итэр (⭐⭐⭐⭐⭐) 💨🗿⚡🌱'},
         'names':{
     'no 4-star archons yet':('\nУвы, 4-звёздночных архонтов пока не существует :(','https://uxwing.com/wp-content/themes/uxwing/download/emoji-emoticon/sad-icon.png'),
    'raiden':('Сёгун Райдэн (⭐⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/9/97/Character_Raiden_Shogun_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205132'),
    'venti':('Венти (⭐⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/9/9e/Character_Venti_Card.png/revision/latest?cb=20220725205218'),
    'zhongli':('Чжун Ли (⭐⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/7/79/Character_Zhongli_Card.png/revision/latest?cb=20201217052506'),
    'nahida':('Нахида (⭐⭐⭐⭐⭐) 🌱','https://static.wikia.nocookie.net/gensin-impact/images/a/ae/Character_Nahida_Card.png/revision/latest/scale-to-width-down/1000?cb=20220926101608'),
    'albedo':('Альбедо (⭐⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/f/f8/Character_Albedo_Card.png/revision/latest?cb=20210302092013'),
    'ganyu':('Гань Юй (⭐⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/8/8d/Character_Ganyu_Card.png/revision/latest/scale-to-width-down/1000?cb=20210106062018'),
    'qiqi':('Ци Ци (⭐⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/b/b7/Character_Qiqi_Card.png/revision/latest?cb=20220725205124'),
    'yanfei':('Янь Фэй (⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/f/f3/Character_Yanfei_Card.png/revision/latest?cb=20210422100113'),
    'shenhe':('Шэнь Хэ (⭐⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/8/83/Character_Shenhe_Card.png/revision/latest?cb=20220725205152'),
    'xiao':('Сяо (⭐⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/8/8e/Character_Xiao_Card.png/revision/latest?cb=20220725205230'),
    'amber':('Амбер (⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/0/04/Character_Amber_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204839'),
    'kaeya':('Кэйа (⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/1/15/Character_Kaeya_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205013'),
    'lisa':('Лиза (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/9/9e/Character_Lisa_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205045'),
    'barbara':('Барбара (⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/4/4a/Character_Barbara_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204852'),
    'bennett':('Беннет (⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/a/ab/Character_Bennett_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204904'),
    'diluc':('Дилюк (⭐⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/7/70/Character_Diluc_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204921'),
    'diona':('Диона (⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/0/08/Character_Diona_Card.png/revision/latest/scale-to-width-down/1000?cb=20201107193459'),
    'eula':('Эола (⭐⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/a/ac/Character_Eula_Card.png/revision/latest/scale-to-width-down/1000?cb=20210511110453'),
    'fischl':('Фишль (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/2/2d/Character_Fischl_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204926'),
    'jean':('Джинн (⭐⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/c/c3/Character_Jean_Card.png/revision/latest?cb=20220725210053'),
    'klee':('Кли (⭐⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/d/dd/Character_Klee_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205026'),
    'mona':('Мона (⭐⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/8/81/Character_Mona_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725210059'),
    'noelle':('Ноэлль (⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/c/c4/Character_Noelle_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205118'),
    'razor':('Рэйзор (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/b/b5/Character_Razor_Card.png/revision/latest?cb=20220725205138'),
    'rosaria':('Розария (⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/6/6d/Character_Rosaria_Card.png/revision/latest/scale-to-width-down/1000?cb=20210330063015'),
    'sucrose':('Сахароза (⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/e/e2/Character_Sucrose_Card.png/revision/latest?cb=20220725205205'),
    'yaoyao':('Яо Яо (⭐⭐⭐⭐) 🌱','https://static.wikia.nocookie.net/gensin-impact/images/b/b2/Character_Yaoyao_Card.png/revision/latest/scale-to-width-down/1000?cb=20221209042817'),
    'chongyun':('Чун Юнь (⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/0/09/Character_Chongyun_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204909'),
    'beidou':('Бэй Доу (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/e/ee/Character_Beidou_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204858'),
    'xinyan':('Синь Янь (⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/e/e1/Character_Xinyan_Card.png/revision/latest/scale-to-width-down/1000?cb=20221121172209'),
    'keqing':('Кэ Цин (⭐⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/b/bd/Character_Keqing_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205019'),
    'hu-tao':('Ху Тао (⭐⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/1/15/Character_Hu_Tao_Card.png/revision/latest?cb=20220725204937'),
    'ningguang':('Нин Гуан (⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/8/89/Character_Ningguang_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205113'),
    'tartaglia':('Тарталья (⭐⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Character_Tartaglia_Card.png/revision/latest?cb=20201106023840'),
    'xiangling':('Сян Лин (⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/e/ed/Character_Xiangling_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205223'),
    'xingqiu':('Син Цю (⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/7/7b/Character_Xingqiu_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205235'),
    'yun-jin':('Юнь Цзинь (⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/1/13/Character_Yun_Jin_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205249'),
    'yelan':('Е Лань (⭐⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/9/98/Character_Yelan_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205242'),
    'arataki-itto':('Аратаки Итто (⭐⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/3/37/Character_Arataki_Itto_Card.png/revision/latest?cb=20220725204845'),
    'kuki-shinobu':('Куки Синобу (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/b/b0/Character_Kuki_Shinobu_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205038'),
    'ayaka':('Камисато Аяка (⭐⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/3/34/Character_Kamisato_Ayaka_Card.png/revision/latest/scale-to-width-down/1000?cb=20210607100828'),
    'ayato':('Камисато Аято (⭐⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/2/22/Character_Kamisato_Ayato_Card.png/revision/latest/scale-to-width-down/1000?cb=20220927195614'),
    'thoma':('Тома (⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/f/f4/Character_Thoma_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205212'),
    'gorou':('Горо (⭐⭐⭐⭐) 🗿','https://static.wikia.nocookie.net/gensin-impact/images/b/b7/Character_Gorou_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725204934'),
    'kazuha':('Кадзуха (⭐⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/2/2d/Character_Kaedehara_Kazuha_Card.png/revision/latest/scale-to-width-down/1000?cb=20210607100841'),
    'shikanoin-heizou':('Хейдзо (⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/9/91/Character_Shikanoin_Heizou_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205159'),
    'kokomi':('Кокоми (⭐⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/8/8c/Character_Sangonomiya_Kokomi_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205145'),
    'sara':('Сара (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/4/46/Character_Kujou_Sara_Card.png/revision/latest/scale-to-width-down/1000?cb=20220725205032'),
    'sayu':('Саю (⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/8/83/Character_Sayu_Card.png/revision/latest/scale-to-width-down/1000?cb=20230121174331'),
    'yae-miko':('Яэ Мико (⭐⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/2/2a/Character_Yae_Miko_Card.png/revision/latest/scale-to-width-down/1000?cb=20211231161334'),
    'yoimiya':('Ёимия (⭐⭐⭐⭐⭐) 🔥','https://static.wikia.nocookie.net/gensin-impact/images/4/4b/Character_Yoimiya_Card.png/revision/latest/scale-to-width-down/1000?cb=20210607100839'),
    'collei':('Коллеи (⭐⭐⭐⭐) 🌱','https://static.wikia.nocookie.net/gensin-impact/images/7/79/Character_Collei_Card.png/revision/latest/scale-to-width-down/1000?cb=20220711041855'),
    'tighnari':('Тигнари (⭐⭐⭐⭐⭐) 🌱','https://static.wikia.nocookie.net/gensin-impact/images/b/b7/Character_Tighnari_Card.png/revision/latest/scale-to-width-down/1000?cb=20220711041536'),
    'candace':('Кандакия (⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/8/8a/Character_Candace_Card.png/revision/latest/scale-to-width-down/1000?cb=20220822101651'),
    'cyno':('Сайно (⭐⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/6/61/Character_Cyno_Card.png/revision/latest/scale-to-width-down/1000?cb=20220822101647'),
    'dori':('Дори (⭐⭐⭐⭐) ⚡','https://static.wikia.nocookie.net/gensin-impact/images/1/11/Character_Dori_Card.png/revision/latest/scale-to-width-down/1000?cb=20220711042206'),
    'faruzan':('Фарузан (⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/genshin-impact/images/4/45/Personagem_Faruzan_Cart%C3%A3o.jpg/revision/latest?cb=20221031183907&path-prefix=pt-br'),
    'layla':('Лайла (⭐⭐⭐⭐) ❄','https://static.wikia.nocookie.net/gensin-impact/images/a/a1/Character_Layla_Card.png/revision/latest/scale-to-width-down/1000?cb=20220926101307'),
    'nilou':('Нилу (⭐⭐⭐⭐⭐) 💧','https://static.wikia.nocookie.net/gensin-impact/images/1/19/Character_Nilou_Card.png/revision/latest/scale-to-width-down/1000?cb=20220822101649'),
    'wanderer':('Странник(⭐⭐⭐⭐⭐) 💨','https://static.wikia.nocookie.net/gensin-impact/images/5/51/Character_Wanderer_Card.png/revision/latest?cb=20221207032514')},
         'text':{
    'starting': 'Добро пожаловать в Симулятор молитв Геншин Импакт!\nДля начала нажмите "Старт"',
    'first_character_choice':'Для начала выбери своего начального персонажа',
    'male':('Поздравляем!\nТы получил своего первого персонажа:\nИтэр (⭐⭐⭐⭐⭐) 💨🗿⚡🌱','https://static.wikia.nocookie.net/shipping/images/1/1c/Traveler_Male_Card.jpg/revision/latest?cb=20210418213306'),
    'female':('Поздравляем!\nТы получил своего первого персонажа:\nЛюмин (⭐⭐⭐⭐⭐) 💨🗿⚡🌱','https://static.wikia.nocookie.net/shipping/images/c/c8/Traveler_Female_Card.jpg/revision/latest?cb=20210407141444'),
    'info':'Для того, чтобы получить других персонажей, тебе надо использовать молитвы.\nВ каждой молитве есть эксклюзивные персонажи, которых можно получить только в этой молитве.\nТвоя задача - постараться выбить как можно больше персонажей.\nУдачи!'},
         'available_characters':[]
}

'''
Использовать, если случайно удалили important_data.json,
     либо хотите сбросить свой прогресс.
     Потом добавлю функцию сброса прогресса, это должно быть легко
'''
# with open('important_data.json','w') as file:
#     json.dump(text_data,file)
    

with open('important_data.json','r') as file:
     data = json.load(file)
     text = data['text']
     characters = data['names']
     banner_info = data['banner_info']
     gallery = data['available_characters']
     banner_details = data['banner_details']

def add_to_gallery(character:str):
     temp_list = []
     with open('important_data.json','r') as file:
          data = json.load(file)
          gallery_here = data['available_characters']
     if len(gallery_here) > 0:
          for i in range(len(gallery_here)):
               temp_list.append(gallery_here[i])
     temp_list.append(character)
     text_data.update({'available_characters':temp_list})
     with open('important_data.json','w') as file:
          json.dump(text_data,file)

def load_gallery() -> str:
     with open('important_data.json','r') as file:
          data = json.load(file)
          loaded_gallery = data['available_characters']
     if len(loaded_gallery) > 0:
          character_list = loaded_gallery[0]
          if len(loaded_gallery) > 1:
               for i in range(1,len(loaded_gallery)):
                    character_list += f'\n{loaded_gallery[i]}'
          return character_list
     else:
          return 'Галерея пока-что пуста ¯\_(ツ)_/¯'

def roll(banner_type:str,pity:int) -> str:
     if pity != 8:
          rarity = '4-star'
     else:
          rarity = '5-star'
     random_character = ran(0,(len(data['banner_drops'][banner_type][rarity]) - 1))
     new_character = data['banner_drops'][banner_type][rarity][random_character]
     new_character_name = characters[new_character][0]
     character_picture = characters[new_character][1]
     return [new_character_name,character_picture]

def is_in_gallery(new_character_name:str) -> bool:
     if new_character_name in load_gallery():
          is_already_exists = True
     else:
          is_already_exists = False
     return is_already_exists