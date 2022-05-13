# Задача 1.6
"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
что перед нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того,
в какой кодировке он был создан.
"""
import chardet


def encoding_detect(file_path):
    """
    :param file_path: путь к файлу, кодировку которого необходимо получить
    :return: код кодировки
    """
    try:
        with open(file_path, 'rb') as f:
            line = f.readline()
        return chardet.detect(line)['encoding']
    except FileNotFoundError:
        print(f'Файл {file_path} не найден')
        return None


def print_lines(file_path):
    """
    Функция выводит содержимое файла вне зависимости от того, в какой кодировке файл был сохранен
    :param file_path: путь к файлу, который необходимо открыть
    """
    # определим кодировку
    encoding = encoding_detect(file_path)
    # читаем данные из файла
    if encoding:
        print(f'Кодировка файла: {encoding}')
        with open(file_path, 'r', encoding=encoding) as f:
            for line in f:
                print(line, end='')


# Пример использования:
print_lines('text_file.txt')

"""
Пример вывода:
    Кодировка файла: UTF-16
    сетевое программирование
    сокет
    декоратор
"""

