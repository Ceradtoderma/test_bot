from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from states import MainState
from bot import bot, dp



class TestState(StatesGroup):
    test_state_inline = State()
    test_state_2 = State()

async def save_data(message: types.Message, state: FSMContext):
    data_dict = await state.get_data()
    data_dict['elements'][message.text.split()[0]] = message.text.split()[1]
    await state.update_data(data=data_dict)
    data = await state.get_data()
    for i in data['elements']:
        await message.answer(f'В словаре записано {i}{data["elements"][i]}')

@dp.callback_query_handler(state=MainState.test_state)
async def answer_inline(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Новая Кнопка 1', callback_data='btn1')
    btn_2 = types.InlineKeyboardButton('Новая Кнопка 2', callback_data='btn2')
    keyboard.add(btn_1, btn_2)
    print(call.message)
    await bot.send_message(chat_id=call.message.chat.id, text='!', reply_markup=keyboard)
    await TestState.test_state_inline.set()




async def get_state(message: types.Message,state: FSMContext):
    state_now = await state.get_state()
    await message.answer(f'текущее состояние {state_now}')

async def get_data(message: types.Message,state: FSMContext):
    data = await state.get_data()
    await message.answer(f'текущее состояние {data}')

async def picture(message: types.Message):
    pic = message
    print(pic)


def register_test_handlers(dp: Dispatcher):
    # dp.register_callback_query_handler(answer_inline, state=MainState.test_state)
    dp.register_message_handler(picture, state=MainState.test_state)
    dp.register_message_handler(get_state, state='*', commands='state')
    # dp.register_message_handler(get_data, state='*', commands='data')

