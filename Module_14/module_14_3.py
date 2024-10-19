from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from time import sleep

from humanfriendly.terminal import message
from pyexpat.errors import messages

api = ''    # Введите ваш ключ TelegramBot
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Формулы расчета'),
         KeyboardButton(text='Рассчитать норму калорий')],
         [KeyboardButton(text='Купить микстуру ВАШ ПОМОШНИК')]
    ],resize_keyboard=True
)
ki = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Для мужчин',callback_data='calories man')],
        [InlineKeyboardButton(text='Для женщин',callback_data='calories woman')]
    ]
)

medicine= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт №1', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт №2', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт №3', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт №4', callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup,):
    age_man = State()
    growth_man = State()
    weight_man = State()
    age_woman = State()
    growth_woman = State()
    weight_woman = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f"Привет, {message.from_user.username}! \n"
                         f"Я Бот, помогающий твоему здоровью", reply_markup=kb)


@dp.message_handler(text='Рассчитать норму калорий')
async def сalculation(message):
    await message.answer("Выберите опцию", reply_markup=ki)

@dp.message_handler(text='Формулы расчета')
async def get_formulas(message):
    await message.answer(f"формула для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n"
                             f"формула для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await message.answer()


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
    sleep(5)    # Просто для создания видимости живой работы бота

    await message.answer(f'Ваша норма Калорий в день - '
                         f'{10 * date["weight"] + 6.25 * date["growth"] + 5 * date["age"] + 5}')
    await  state.finish()

@dp.message_handler(state=UserState.weight_woman )
async def time_aut_woman(message, state):
    await state.update_data(weight= int(message.text))
    date = await state.get_data()
    await message.answer(f'Подождите, идет расчет калорий.')
    sleep(5)    # Просто для создания видимости живой работы бота
    await message.answer(f'Ваша норма Калорий в день - '
                         f'{10 * date["weight"] + 6.25 * date["growth"] + 5 * date["age"] - 161}')
    await  state.finish()

@dp.message_handler( text="Купить микстуру ВАШ ПОМОШНИК" )
async def get_buying_list(message):
    with open('file/medicine1.jpg', "rb") as img:
            await  message.answer_photo(img, "Продукт №1. \n"
                                            "подойдет для тех, кому нравится свое тело\n"
                                            "Цена 1000 руб")

    with open( 'file/medicine2.jpg', "rb" ) as img:
            await  message.answer_photo( img, "Продукт №2. \n"
                                            "подойдет для тех, кто хочет скинуть до 5 кг.\n"
                                            "Цена 1100 руб")
    with open( 'file/medicine3.jpg', "rb" ) as img:
            await  message.answer_photo( img, "Продукт №3. \n"
                                            "подойдет для тех, кто хочет скинуть более 5 кг.\n"
                                            "Цена 1200 руб")
    with open( 'file/medicine4.jpg', "rb" ) as img:
            await  message.answer_photo( img, "Продукт №4. \n"
                                            "подойдет для тех, кто хочет набрать вес.\n"
                                            "Цена 1300 руб")

    await message.answer( "Выберите микстуру, которую хотите купить",
                                  reply_markup=medicine )

@dp.callback_query_handler( text="product_buying")
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Напишите "/start", чтобы начать')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)