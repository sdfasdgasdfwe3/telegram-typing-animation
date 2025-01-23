import logging
from telethon import TelegramClient

# Логирование
logging.basicConfig(level=logging.INFO)

def test_module(client: TelegramClient):
    """
    Этот модуль тестирует работу бота, отправляя сообщение в Telegram.
    :param client: Экземпляр клиента Telegram
    """
    try:
        # Отправляем сообщение в первый доступный чат
        message = "Модуль успешно установлен и работает!"
        async def send_message():
            # Получаем список чатов
            dialogs = await client.get_dialogs()
            # Проверяем, есть ли хотя бы один чат
            if dialogs:
                # Отправляем сообщение в первый найденный чат
                await client.send_message(dialogs[0].entity.id, message)
                print(f"Сообщение успешно отправлено: {message}")
            else:
                print("Не удалось найти чаты для отправки сообщения.")
        
        # Запуск асинхронной функции отправки сообщения
        client.loop.run_until_complete(send_message())
    
    except Exception as e:
        logging.error(f"Ошибка в работе модуля: {e}")
        print(f"Ошибка в работе модуля: {e}")
