from aiogram import types

start = types.InlineKeyboardMarkup()
buttons = [
    types.InlineKeyboardButton('Парсер', callback_data='parser'),
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

keyboards = {
    'start': start,
    'weather_day': weather_day,
    'parser_start': parser_start,
    'parser_auth': parser_auth,
    'parser_login': parser_login,

}
