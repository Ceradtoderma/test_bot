from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import keyboards
from bot import bot, dp, MainState



@dp.message_handler(commands='start', state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await MainState.main_state.set()
    await message.answer('Реакция на команду /start', reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Что делаем?", reply_markup=keyboards['start'])


@dp.callback_query_handler(lambda c: c.data == 'gui_btn', state='*')
async def gui_button(call: types.CallbackQuery):
    await call.message.answer('Удаленный ввод текста')




@dp.message_handler()
async def error(message: types.Message, state: FSMContext):
    await message.answer('Ты ввёл что-то неправильно. Давай еще раз расскажу,что я могу!',
                         reply_markup=keyboards['start'])
    await MainState.main_state.set()


