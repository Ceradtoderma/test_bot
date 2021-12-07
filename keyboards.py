from aiogram import types


start = types.InlineKeyboardMarkup()
buttons = [
    types.InlineKeyboardButton('Кнопка GUI', callback_data='gui_btn'),


]
start.add(*buttons)

weather_day = types.InlineKeyboardMarkup()
buttons = [
    types.InlineKeyboardButton('Сегодня', callback_data='0'),
    types.InlineKeyboardButton('Завтра', callback_data='1'),
    types.InlineKeyboardButton('Послезавтра', callback_data='2'),
]
weather_day.add(*buttons)

parser_start = types.InlineKeyboardMarkup()
parser_start.add(types.InlineKeyboardButton('Начать парсинг', callback_data='start_parsing'))

parser_auth = types.InlineKeyboardMarkup()
parser_auth.add(types.InlineKeyboardButton('С логином', callback_data='login'))
parser_auth.add(types.InlineKeyboardButton('Без логина', callback_data='without_login'))

parser_login = types.InlineKeyboardMarkup()
parser_login.add(types.InlineKeyboardButton('Попробовать залогинится', callback_data='login'))

cheese_start = types.InlineKeyboardMarkup()
cheese_start.add(types.InlineKeyboardButton('Все сыры', callback_data='all_cheese'))
cheese_start.add(types.InlineKeyboardButton('Добавить сыр', callback_data='add_cheese'))
cheese_start.add(types.InlineKeyboardButton('Посмотреть конкретный', callback_data='one_cheese'))

keyboards = {
    'start': start,
    'weather_day': weather_day,
    'parser_start': parser_start,
    'parser_auth': parser_auth,
    'parser_login': parser_login,
    'cheese_start': cheese_start,

}
