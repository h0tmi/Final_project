import logging
import typing
from time import sleep
from googlesearch import search
import wikipedia

import aiogram.utils.markdown as md
import pandas as pd
import numpy as np

from aiogram import Bot, Dispatcher, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.markdown import text
from config import TOKEN
from functions import MESSAGES
from States import TestStates
import keyboard as kb
import googletrans

import klasters as ks

logging.basicConfig(level=logging.INFO)
# token
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


###################################################
# await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
###################################################
    # for i in search(u_name + ' смотреть', tld="co.in", num=10, stop=1, pause=2):
    #     print(i)
###################################################
@dp.message_handler(commands = ['start'])
async def start_command(message = types.Message):
    # Приветствие, спросить смотрел он аниме раньше или нет
    # дальше кидаем опросник
    print(message.from_user.id)
    print(message)
    await bot.send_message(message.from_user.id, MESSAGES['start'], reply_markup=kb.inline_kb_get)



@dp.callback_query_handler(text = 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.callback_query_handler(text = 'get')
async def process_callback_get(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, ks.get_the_best(callback_query.from_user.id))



@dp.message_handler(commands = ['info'])
async def info_command(message = types.Message):
    # Информация о пользователе
    # сколько посмотрел, что смотрел, какие оценки и т.п.
    await message.reply(MESSAGES['info'])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)

