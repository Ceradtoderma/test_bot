from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from states import MainState
from autor_today.pars_handlers import register_pars_handlers
from keyboards import keyboards


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await MainState.main_state.set()
    await message.answer('Реакция на команду /start')
    await message.answer("Что делаем?", reply_markup=keyboards['start'])



async def inline_answer(call: types.CallbackQuery):

    if call.data == 'parser':
        await MainState.parser_state.set()
        await call.answer('Попробуем украсть книжку')
        await call.message.answer('Переходим в режим парсера сайта Autor.today', reply_markup=keyboards['parser_auth'])



async def error(message: types.Message, state: FSMContext):
    await message.answer('Ты ввёл что-то неправильно. Давай еще раз расскажу,что я могу!',
                         reply_markup=keyboards['start'])
    await MainState.main_state.set()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
    dp.register_callback_query_handler(inline_answer, state=MainState.main_state)
    register_pars_handlers(dp)
    dp.register_message_handler(error, state='*')