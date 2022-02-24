from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_1 = InlineKeyboardButton('Давай!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_btn_get = InlineKeyboardButton('Порекомендовать', callback_data='get')
inline_kb_get = InlineKeyboardMarkup().add(inline_btn_get)

inline_kb_first = InlineKeyboardMarkup()
inline_btn_find = InlineKeyboardButton('Начать', callback_data='start')
inline_btn_none = InlineKeyboardButton('Я ничего не смотрел', callback_data='None')
inline_kb_first.add(inline_btn_find, inline_btn_none)

# review + site in main
inline_kb_ch = InlineKeyboardMarkup()
inline_b_rec = InlineKeyboardButton('Порекомендовать', callback_data='rec')
inline_b_ch = InlineKeyboardButton('Ввести аниме', callback_data='choose')
inline_kb_ch.add(inline_b_ch, inline_b_rec)