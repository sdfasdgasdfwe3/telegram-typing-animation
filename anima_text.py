import time

def typewriter_effect(text, speed=0.05, cursor="|", end="\n"):
    """
    Печатает текст с эффектом печатающей машинки.
    :param text: Текст для вывода
    :param speed: Скорость печати (в секундах между символами)
    :param cursor: Символ курсора, отображаемый в конце строки
    :param end: Символ, добавляемый в конце анимации (по умолчанию новая строка)
    """
    result = ""
    for char in text:
        result += char
        time.sleep(speed)
    return result + cursor + end

def loading_animation(message="Loading", dots=3, speed=0.5):
    """
    Показывает анимацию загрузки с точками.
    :param message: Сообщение перед точками
    :param dots: Количество точек в анимации
    :param speed: Скорость анимации (в секундах между изменениями)
    """
    result = ""
    for _ in range(dots):
        result = f"{message}{'.' * _}\n"
        time.sleep(speed)
    return result + "Готово!"

# Список доступных анимаций
animations = {
    "1": "Эффект печатающей машинки",
    "2": "Анимация загрузки"
}

def get_animations():
    """Возвращает список анимаций для пользователя."""
    return "\n".join([f"{key}. {value}" for key, value in animations.items()])

