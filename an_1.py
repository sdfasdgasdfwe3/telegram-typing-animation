import sys
import time

def typewriter_effect(text, speed=0.05, cursor="|", end="\n"):
    """
    Печатает текст с эффектом печатающей машинки.
    
    :param text: Текст для вывода
    :param speed: Скорость печати (в секундах между символами)
    :param cursor: Символ курсора, отображаемый в конце строки
    :param end: Символ, добавляемый в конце анимации (по умолчанию новая строка)
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    
    # Добавляем курсор на короткое время
    sys.stdout.write(cursor)
    sys.stdout.flush()
    time.sleep(0.3)
    
    # Убираем курсор и завершаем анимацию
    sys.stdout.write("\b \b" + end)
    sys.stdout.flush()

def loading_animation(message="Loading", dots=3, speed=0.5):
    """
    Показывает анимацию загрузки с точками.
    
    :param message: Сообщение перед точками
    :param dots: Количество точек в анимации
    :param speed: Скорость анимации (в секундах между изменениями)
    """
    for _ in range(dots):
        sys.stdout.write(f"\r{message}{'.' * _}")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\r" + " " * (len(message) + dots) + "\r")  # Очистка строки

if __name__ == "__main__":
    # Пример использования
    typewriter_effect("Привет! Это пример текста с анимацией.\n", speed=0.07)
    loading_animation("Загрузка", dots=5, speed=0.4)
    print("Готово!")
