from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram

api = '7278751243:AAHx3xwPDpqL6TxF-bfBQ6t3Ha9ZDA9A98Y'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# @dp.message_handler()
# async def all_messages(message):
#      print('Мы получили сообщение')

@dp.message_handler(text= ['Привет', 'Пока'])
async def text_message(message):
    print('text_message')

@dp.message_handler(commands= ['start'])
async def commands_message(message):
    print('commands_message')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
