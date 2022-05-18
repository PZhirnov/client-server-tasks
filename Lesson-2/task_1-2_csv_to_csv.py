"""
Вариант 2 для задачи №1
Более универсальный в использвоании, учитывая возможность добавления нужных полей
"""

from chardet import detect
import csv
import re


LIST_FILE_NAMES = [
    'info_1.txt',
    'info_2.txt',
    'info_3.txt'
]
LIST_GET_FIELDS = [
    'Название ОС',
    'Изготовитель системы',
    'Код продукта',
    'Тип системы',
    'Процессор(ы)',  # пример поля со спецсимволом
]


def get_data(list_files, list_fields):
    """
    Формирует данные для записи
    :return: данные в виде списка списков
    """
    # Создал списки по условию задачи
    main_data = []
    for file_name in list_files:
        # Прочитаем данные из файла
        with open(file_name, 'rb') as f:
            encoding = detect(f.read())['encoding']
            f.seek(0)
            content = f.read().decode(encoding=encoding)
        row_data = []
        for field in list_fields:
            field = re.escape(field)
            pattern = rf"{field}:(?:\W+)(.*?)\r"
            result = re.search(pattern, content, re.IGNORECASE)
            row_data.append(result.groups()[0].strip() if result else 'n/a')
        main_data.append(row_data)
    main_data = [LIST_GET_FIELDS, *main_data]
    return main_data if main_data else None


def write_to_csv(fpath):
    """
    Запись данных в файл csv
    :param fpath: полное имя создаваемого файла
    """
    data = get_data(LIST_FILE_NAMES, LIST_GET_FIELDS)
    if not data:
        return 'Данные не были получены'
    with open(fpath, 'w', encoding='utf-8', newline='') as f:
        file_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        file_writer.writerows(data)


write_to_csv('task_1-2_write.csv')
