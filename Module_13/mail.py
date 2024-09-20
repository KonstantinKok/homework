from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram
from babel.dates import date_
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = '7278751243:AAHx3xwPDpqL6TxF-bfBQ6t3Ha9ZDA9A98Y'    # Введите ваш ключ TelegramBot
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text= 'Информация')
button2 = KeyboardButton(text= 'Начало')
kb.add(button)    #kb.row   kb.insert - другие варианты добавления кнопки
kb.add(button2)

@dp.message_handler(commands=['start'])
async def start(message):
       await message.answer('Hello', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация о боте')
    

# class UserState(StatesGroup):
#     adress = State()
#
# @dp.message_handler(text= ['Заказать'])
# async def byu(message):
#     await message.answer('Привет! Отправь нам свой адрес')
#     await UserState.adress.set()
#
# @dp.message_handler(state=UserState.adress)
# async def fsm_handler(message, state):
#     await state.update_data(first= message.text)
#     date = await state.get_data()
#     await message.answer(f'Доставка будет по адресу {date["first"]}')
#     await  state.finish()

# @dp.message_handler()
# async def all_messages(message):
#       await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
