from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from time import sleep

from pyexpat.errors import messages

api = ''    # Введите ваш ключ TelegramBot
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
button2 = InlineKeyboardButton(text='Мужской',callback_data='calories man')
button3 = InlineKeyboardButton(text='Женский',callback_data='calories woman')
kb.add(button1)
kb.add(button2)
kb.add(button3)

class UserState(StatesGroup,):
    age_man = State()
    growth_man = State()
    weight_man = State()
    age_woman = State()
    growth_woman = State()
    weight_woman = State()


@dp.message_handler(text=['Расчитать'])
async def start(message):
    await message.answer("Выбирите опцию", reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(f"формула для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n"
                             f"формула для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await call.answer()


@dp.callback_query_handler(text= ['calories man'])
async def set_age_man(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age_man.set()

@dp.callback_query_handler(text= ['calories woman'])
async def set_age_woman(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age_man.set()



@dp.message_handler(state=UserState.age_man )
async def set_growth_man(message, state):
    await state.update_data(age= int(message.text))
    date = await state.get_data()
    await message.answer('Введите свой рост')
    await UserState.growth_man.set()

@dp.message_handler(state=UserState.age_woman )
async def set_growth_woman(message, state):
    await state.update_data(age= int(message.text))
    date = await state.get_data()
    await message.answer('Введите свой рост')
    await UserState.growth_woman.set()



@dp.message_handler(state=UserState.growth_man )
async def set_weight_man(message, state):
    await state.update_data(growth= int(message.text))
    date = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight_man.set()

@dp.message_handler(state=UserState.growth_woman )
async def set_weight_woman(message, state):
    await state.update_data(growth= int(message.text))
    date = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight_woman.set()



@dp.message_handler(state=UserState.weight_man )
async def time_aut_man(message, state):
    await state.update_data(weight= int(message.text))
    date = await state.get_data()
    await message.answer(f'Подождите, идет расчет калорий.')
    sleep(5)    # Просто для создания видимости живой работы бота)
    await message.answer(f'Ваша норма Калорий в день - '
                         f'{10 * date["weight"] + 6.25 * date["growth"] + 5 * date["age"] + 5}')
    await  state.finish()

@dp.message_handler(state=UserState.weight_woman )
async def time_aut_woman(message, state):
    await state.update_data(weight= int(message.text))
    date = await state.get_data()
    await message.answer(f'Подождите, идет расчет калорий.')
    sleep(5)    # Просто для создания видимости живой работы бота)
    await message.answer(f'Ваша норма Калорий в день - '
                         f'{10 * date["weight"] + 6.25 * date["growth"] + 5 * date["age"] - 161}')
    await  state.finish()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Напишите "Расчитать", чтобы начать')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
