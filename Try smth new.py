import pandas as pd

from googletrans import Translator
from googlesearch import search
import wikipedia as wk


def AnimeSearch(u_name='Твоё имя'):
    anime_list = pd.read_csv('anime.csv')
    anime_list = anime_list['name']
    wk.set_lang('ru')
    wk.set_lang('en')
    print(wk.search(u_name ))


while True:
    s = input()
    if AnimeSearch(s):
        print("Found")
    else:
        print("ooops")