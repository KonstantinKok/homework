from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram

api = 'YOU KEY'    # Введите ваш ключ
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text= ['Привет', 'Пока'])
async def text_message(message):
    print('text_message')

@dp.message_handler(commands= ['start'])
async def commands_message(message):
    print('commands_message')

@dp.message_handler()
async def all_messages(message):
      print('Мы получили сообщение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
