from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from babel.dates import date_
from time import sleep


api = '7278751243:AAHx3xwPDpqL6TxF-bfBQ6t3Ha9ZDA9A98Y'    # Введите ваш ключ TelegramBot
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text= ['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age )
async def set_growth(message, state):
    await state.update_data(age= message.text)
    date = await state.get_data()
    await message.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth )
async def set_weight(message, state):
    await state.update_data(growth= message.text)
    date = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight )
async def time_aut(message, state):
    await state.update_data(weight= message.text)
    date = await state.get_data()
    await message.answer('Подождите, идет расчет калорий.....')
    sleep(6)
    await message.answer(f'Ваша норма Калорий - {date[10 * "weight" + 6,25 * "growth" + 5 * "age" + 5]}')
    await  state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
