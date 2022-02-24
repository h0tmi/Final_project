from utils import TestStates


info_message = 'Тут крч инфа за пользователя'

start_message = 'Привет, я вижу, что ты здесь впервые, давай заполним анкету твоих предпочтений'
# invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
# state_change_success_message = 'Текущее состояние успешно изменено'
# state_reset_message = 'Состояние успешно сброшено'
# current_state_message = 'Текущее состояние - "{current_state}", что удовлетворяет условию "один из {states}"'

go_message = 'Назови мне 3 аниме, которые понравились тебе больше всего. Только пиши пиши на английском и в разных сообщениях!!! Аккуратно, я бот, я не понимаю ошибок в словах, почти)'

ask_message = 'Отправь мне назвнания трёх твоих любимых аниме на английском, если ты не можешь определиться я могу предложить мои)'

first_recommend_anime = "Жаль, что ты не смотрел аниме раньше, тогда давай начнём с чего-то хорошего:"

recommend_anime = 'Попробуй посмотреть вот это и скажи мне как оно тебе:'
syl = 'Надеюсь я смог порекомендовать тебе что-то достойное, увидемся позже.\nЕсли вдруг захочешь ещё рекомендаций, напиши мне /new_anime'
MESSAGES = {
    'start': start_message,
    'info': info_message,
    'go' : go_message,
    'ask' : ask_message,
    'f_rec' : first_recommend_anime,
    'rec' : recommend_anime,
    'syl' : syl
    # 'invalid_key': invalid_key_message,
    # 'state_change': state_change_success_message,
    # 'state_reset': state_reset_message,
    # 'current_state': current_state_message,
}