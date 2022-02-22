from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_btn_get = InlineKeyboardButton('Порекомендовать', callback_data='get')
inline_kb_get = InlineKeyboardMarkup().add(inline_btn_get)

