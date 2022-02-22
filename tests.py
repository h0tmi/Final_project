import logging
import typing
from time import sleep
from googlesearch import search
import wikipedia

from functions import *
import aiogram.utils.markdown as md
import pandas as pd
import numpy as np

anime = pd.read_csv("anime.csv")

print(anime.head(10)['name'])



# работа с бд возможно и картинками

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
#
# class MediaIds(Base):
#     __tablename__ = 'Media ids'
#     id = Column(Integer, primary_key=True)
#     file_id = Column(String(255))
#     filename = Column(String(255))

# https://github.com/mahenzon/aiogram-lessons/blob/master/lesson-02/upload_my_files.py
# скрипт, с помощью которого можно будет добавлять всё в бд
