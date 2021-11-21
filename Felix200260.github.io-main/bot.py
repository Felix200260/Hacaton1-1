import os
import time
import numpy as np
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
import logging
from typing import List, NamedTuple, Optional

bot = Bot(token='2109404541:AAEr6uDtGxZo6yDJE9QVisvEvcAtq-aN2YY')

dp = Dispatcher(bot, storage=MemoryStorage())

amount = np.array([])
debter = np.array([])
casher = np.array([])


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        'Привет! Я - ГДЛ. Вы можете воспользоваться мной для распределения долгов в компании друзей.\nЧего хотите?\n1)Добавить должника /add\n2)Все должники /all \n3)Поиск должника по имени /find\n4)Погасить долг /ret\n5)Список друзей /friends')


@dp.message_handler(commands=['help'])
async def menu(message: types.Message):
    await message.answer('Мои функции:\n1)Добавить должника\n2)Все должники\n3)Поиск по должнику\n4)Погасить долг')

@dp.message_handler(commands=['friends'])
async def menu(message: types.Message):
    await message.answer('Ваши друзья\n@Ivan\n@Dmitry') #откуда-то брать данные

@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    await message.answer(
        'Введите данные должника в следующей форме:\nЦена товара имена_должников\nНапример: 100 user user ...')
    s = message.text
    await message.answer(s)

#@dp.message_handler(commands=['all'])
# async def show(message: types.Message):
#     if not amount:
#         await message.answer('Никто никому ничего не должен')
#     else:
#         await message.answer('Сколько - кто - кому')
#         for i in range(len(amount)):
#             print(amount[i], ' - ', debter[i], ' - ', casher[i])

@dp.message_handler(commands=['all'])
async def show(message: types.Message):
    await message.answer('@Ivan должен 100 @Maxim\n@Dmitry должен 100 @Maxim')

@ dp.message_handler(commands=['find'])
async def person(message: types.Message):
    await message.answer('Введи имя должника:')
    name = message.text
    await message.reply('Сколько - кому')
    temp = np.where(debter == name)
    if not temp:
        await message.answer('Таких должников нет')
    else:
        for i in range(len(temp)):
            print(amount[temp[i]], ' - ', casher[temp[i]])


@dp.message_handler(commands=['ret'])
async def minus(message: types.Message):
    # await message.answer('Чей долг погасить?')
    name = message.text
    temp = np.where(debter == name)
    if not temp:
        await message.answer('Таких должников нет')
    else:
        await message.answer('Сколько денег он вернул?')
        summ = message.text
        while summ.isdigit == FALSE:
            await message.answer('Неверный формат, попробуйте снова')
            summ = message.text
        else:
            while summ != 0:
                index = debter.index(name)
                if (amount[index] <= summ):
                    summ -= amount[index]
                    amount.pop(index)
                    debter.pop(index)
                    casher.pop(index)
                else:
                    amount[index] -= summ
                    summ = 0



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)