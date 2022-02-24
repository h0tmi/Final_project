import logging
import typing
from time import sleep

from utils import TestStates
from googlesearch import search
import wikipedia

import aiogram.utils.markdown as md
import pandas as pd
import numpy as np

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


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
from utils import TestStates
import keyboard as kb
import wikipedia as wk

from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton

import klasters as ks
# ks.upd()
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

wk.set_lang('ru')
global anime_nm
anime_nm = 'Death Note'
global user_list
user_list = list(list())
global u_cnt
u_cnt = 0

global st
st = 0

inline_kb_top = InlineKeyboardMarkup()


inline_kb_review = InlineKeyboardMarkup()

b1 = InlineKeyboardButton('1', callback_data='1')
b2 = InlineKeyboardButton('2', callback_data='2')
b3 = InlineKeyboardButton('3', callback_data='3')
b4 = InlineKeyboardButton('4', callback_data='4')
b5 = InlineKeyboardButton('5', callback_data='5')
b6 = InlineKeyboardButton('6', callback_data='6')
b7 = InlineKeyboardButton('7', callback_data='7')
b8 = InlineKeyboardButton('8', callback_data='8')
b9 = InlineKeyboardButton('9', callback_data='9')
b10 = InlineKeyboardButton('10', callback_data='10')
inline_kb_review = InlineKeyboardMarkup(row_width=5)
inline_kb_review.add(b1, b2, b3, b4, b5)
inline_kb_review.add(b6, b7, b8, b9, b10)


b1 = InlineKeyboardButton('1', callback_data='1')
b2 = InlineKeyboardButton('2', callback_data='2')
b3 = InlineKeyboardButton('3', callback_data='3')
b4 = InlineKeyboardButton('4', callback_data='4')
b5 = InlineKeyboardButton('5', callback_data='5')
b6 = InlineKeyboardButton('6', callback_data='6')
b7 = InlineKeyboardButton('7', callback_data='7')
b8 = InlineKeyboardButton('8', callback_data='8')
b9 = InlineKeyboardButton('9', callback_data='9')
b10 = InlineKeyboardButton('10', callback_data='10')

inline_kb_top.add(b1, b2, b3, b4, b5)
inline_kb_top.add(b6, b7, b8, b9, b10)

for i in search(anime_nm + ' смотреть', tld="co.in", num=10, stop=1, pause=2):
    site = InlineKeyboardButton('Перейти на сайт', url=i, callback_data='site')
    done = InlineKeyboardButton('Я не хочу больше искать', callback_data='done')
    inline_kb_review.add(site, done)
    break

def check(s1, s2):
    cnt = 0
    s1 = s1.lower()
    s2 = s2.lower()

    l1 = list()
    for i in range(0, 200):
        l1.append(0)
    l2 = list()
    for i in range(0, 200):
        l2.append(0)
    for i in s1:
        if ord(i) < 200:
            l1[int(ord(i))] += 1
    for j in s2:
        if ord(j) < 200:
            l2[int(ord(j))] += 1
    for i in range(0, 200):
        cnt += abs(l1[i] - l2[i])

    return cnt


def AnimeSearch(u_name='Твоё имя'):
    anime_list = pd.read_csv('anime.csv')
    anime_list = anime_list['name']
    cnt = int(1e9 + 7)
    name = ''
    for i in anime_list:
        cur = check(i, u_name)
        if cur < cnt:
            cnt = cur
            name = i
        # if cur:
        #     print(str(cur) + ' ' + i)
    return name

###################################################
@dp.message_handler(commands=['start'])
async def start_command(message=types.Message):
    # Приветствие, спросить смотрел он аниме раньше или нет
    # дальше кидаем опросник
    print(message.from_user.id)
    print(message)
    await bot.send_message(message.from_user.id, MESSAGES['start'],
                           reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['new_anime'])
async def start_command(message=types.Message):
    # Приветствие, спросить смотрел он аниме раньше или нет
    # дальше кидаем опросник
    print(message.from_user.id)
    print(message)
    await bot.send_message(chat_id=message.from_user.id,
                                text='Я думаю...')
    global anime_nm
    anime_nm = ks.get_the_best(message.from_user.id)
    cur = wikipedia.search(anime_nm)
    cur = cur[0]
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)
    cur = wikipedia.search(anime_nm)
    cur = cur[0]
    await bot.send_message(message.from_user.id,
                           MESSAGES['rec'] + "\n" + wk.page(cur).summary[
                                                    :wk.page(cur).summary[
                                                     200:].find('\n') + 200],
                           reply_markup=inline_kb_review)


@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    # add user to was list
    await bot.send_message(callback_query.from_user.id, MESSAGES['go'],
                           reply_markup=kb.inline_kb_first)


@dp.callback_query_handler(text='done')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           MESSAGES['syl'])  # see you later


@dp.callback_query_handler(text='start')
async def process_callback_button1(callback_query: types.CallbackQuery):
    # states
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['ask'],
                           reply_markup=kb.inline_kb_ch)
    # user id
###########################################################################
@dp.callback_query_handler(state='*', text='choose')
async def process_callback_button1(callback_query: types.CallbackQuery):
    # states
    await bot.answer_callback_query(callback_query.id)
    # state = dp.current_state(user=callback_query.message.from_user.id)
    # await bot.delete_message(chat_id=callback_query.message.chat.id,
    #                          message_id=callback_query.message.message_id)
    # await bot.send_message(callback_query.from_user.id, MESSAGES['ask'],
    #                        reply_markup=kb.inline_kb_ch)
    # user id
    # user_list.append({"", "", ""})
    # cnt += 1
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text="Теперь вводи аниме)")
    state = dp.current_state(user=callback_query.from_user.id)
    await state.set_state(TestStates.all()[1])
    print("Choosing")


@dp.message_handler(state=TestStates.TEST_STATE_1)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestStates.all()[2])
    print(message.text)
    anime_cur = AnimeSearch(message.text)
    global anime_nm
    anime_nm = anime_cur
    await bot.send_message(chat_id=message.chat.id, text='Записал тебе - ' + str(anime_cur), reply_markup=inline_kb_top)


@dp.message_handler(state=TestStates.TEST_STATE_2)
async def second_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestStates.all()[3])
    print(message.text)
    anime_cur = AnimeSearch(message.text)
    global anime_nm
    anime_nm = anime_cur
    await bot.send_message(chat_id=message.chat.id, text='Записал тебе - ' + anime_cur, reply_markup=inline_kb_top)


@dp.message_handler(state=TestStates.TEST_STATE_3)
async def third_or_fourth_test_state_case_met(message: types.Message):
    print(message.text)
    anime_cur = AnimeSearch(message.text)
    await bot.send_message(chat_id=message.chat.id, text='Записал тебе - ' + anime_cur, reply_markup=inline_kb_top)
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Я думаю...')
    global anime_nm
    anime_nm = anime_cur
    cur = wikipedia.search(anime_nm)
###########################################################################

@dp.callback_query_handler(text='None')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text='Я думаю...')
    global anime_nm
    anime_nm = ks.get_the_best(callback_query.from_user.id)
    cur = wikipedia.search(anime_nm)
    cur = cur[0]
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           MESSAGES['f_rec'] + "\n" + wk.page(cur).summary[
                                                      :wk.page(cur).summary[
                                                       200:].find('\n') + 200],
                           reply_markup=inline_kb_review)

@dp.callback_query_handler(state=TestStates.TEST_STATE_1 | TestStates.TEST_STATE_2 | TestStates.TEST_STATE_3,
    text=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
async def process_callback_button1(callback_query: types.CallbackQuery):
    rated = callback_query.data  # for kmeans
    global anime_nm
    ks.add(anime_nm, callback_query.from_user.id, int(rated))
    global st
    st += 1
    # print(dp.current_state(user=callback_query.from_user.id).get_state())
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text='Записал твою оценку.')
    if st == 3:
        st = st % 3
        await dp.current_state(user=callback_query.from_user.id).reset_state()
        # await bot.delete_message(chat_id=message.chat.id,
        #                          message_id=message.message_id + 2)
        # global anime_nm
        anime_nm = ks.get_the_best(callback_query.from_user.id)
        cur = wikipedia.search(anime_nm)
        cur = cur[0]
        await bot.send_message(callback_query.from_user.id,
                               MESSAGES['rec'] + "\n" + wk.page(cur).summary[
                                                        :wk.page(cur).summary[
                                                         200:].find(
                                                            '\n') + 200],
                               reply_markup=inline_kb_review)
    await bot.answer_callback_query(callback_query.id)

# @dp.callback_query_handler(text = 'get')
# async def process_callback_get(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, ks.get_the_best(callback_query.from_user.id))

@dp.callback_query_handler(
    text=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'rec'])
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.data != 'rec':
        rated = callback_query.data  # for kmeans
        global anime_nm
        ks.add(anime_nm, callback_query.from_user.id, int(rated))

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id, text='Я думаю...')
    # global anime_nm
    anime_nm = ks.get_the_best(callback_query.from_user.id)
    cur = wikipedia.search(anime_nm)
    cur = cur[0]
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                           text=MESSAGES['rec'] + "\n" + wk.page(cur).summary[
                                                    :wk.page(cur).summary[
                                                     200:].find('\n') + 200],
                           reply_markup=inline_kb_review)


@dp.message_handler(commands=['info'])
async def info_command(message=types.Message):
    # Информация о пользователе
    # сколько посмотрел, что смотрел, какие оценки и т.п.
    await message.reply(MESSAGES['info'])


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
