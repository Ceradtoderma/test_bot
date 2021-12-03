from aiogram.dispatcher.filters.state import State, StatesGroup


class MainState(StatesGroup):
    main_state = State()
    parser_state = State()
    cheese_state = State()
    test_state = State()