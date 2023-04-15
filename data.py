from aiogram.types import *

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
buy_guides_btn = KeyboardButton('Выбрать курс')
connect_support_btn = KeyboardButton('Связаться с поддержкой')
main_menu_kb.add(buy_guides_btn, connect_support_btn)

buy_guides_ikb = InlineKeyboardMarkup(row_width=1)
maths_guide_btn = InlineKeyboardButton('Курс по математике', callback_data='maths')
informatics_guide_btn = InlineKeyboardButton('Курс по информатике', callback_data='info')
physics_guide_btn = InlineKeyboardButton('Курс по физике', callback_data='physics')
buy_guides_ikb.add(maths_guide_btn, informatics_guide_btn, physics_guide_btn)

guides_data = {
    'maths': {'title': 'Курс по математике', 'desc': 'Курс по математике(Теория Вероятности и Статистика)', 'photo_url': 'https://cdn-icons-png.flaticon.com/512/746/746961.png', 'price': [LabeledPrice(label='Курс по Математике', amount=50000)], 'payload': 'maths.pdf'},
    'info': {'title': 'Курс по информатике', 'desc': 'Курс по информатике(основы Python)', 'photo_url': 'https://cdn-icons-png.flaticon.com/512/5381/5381431.png', 'price': [LabeledPrice(label='Курс по Информатике', amount=75000)], 'payload': 'infos.pdf'},
    'physics': {'title': 'Курс по физике', 'desc': 'Курс по физике', 'photo_url': 'https://cdn-icons-png.flaticon.com/512/2219/2219150.png', 'price': [LabeledPrice(label='Курс по Физике', amount=100000)], 'payload': 'physics.pdf'}
}
