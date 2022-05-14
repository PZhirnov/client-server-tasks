# Задача 1.5
"""
Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат
из байтовового типа данных в строковый без ошибок для любой кодировки операционной системы.
"""

import chardet
import subprocess
import platform


def ping(url, num_ping=2):
    """
    Функция выводит результат ping в консоль
    :param url: адрес, на который отправляем ping
    :param num_ping: количество ping
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, str(num_ping), url]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        # print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'), end='')


# Проверка работоспособности по условиям задачи
ping('yandex.ru', 5)
ping('youtube.com', 5)
