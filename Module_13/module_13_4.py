from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from time import sleep


api = ''    # Введите ваш ключ TelegramBot
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
    await state.update_data(age= int(message.text))
    date = await state.get_data()
    await message.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth )
async def set_weight(message, state):
    await state.update_data(growth= int(message.text))
    date = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight )
async def time_aut(message, state):
    await state.update_data(weight= int(message.text))
    date = await state.get_data()
    await message.answer(f'Подождите, идет расчет калорий.')
    sleep(5)    # Просто для создания видимости живой работы бота)
    await message.answer(f'Ваша норма Калорий - '
                         f'{10 * date["weight"] + 6.25 * date["growth"] + 5 * date["age"] + 5}')
    await  state.finish()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду Calories, чтобы начать общение')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

