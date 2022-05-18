"""
Задание №1. Решение в соответствии с условием

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
]


def get_data():
    """
    Формирует данные для записи
    :return:
    """
    # Создал списки по условию задачи
    main_data = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file_name in LIST_FILE_NAMES:
        # Прочитаем данные из файла
        with open(file_name, 'rb') as f:
            encoding = detect(f.read())['encoding']
            f.seek(0)
            content = f.read().decode(encoding=encoding)

        def get_value_field(field_name):
            field_name = re.escape(field_name)
            pattern = rf"{field_name}:(?:\W+)(.*?)\r"
            result = re.search(pattern, content, re.IGNORECASE)
            return result.groups()[0].strip() if result else None
        # Добавляем данные в соответствующие списки
        os_prod_list.append(get_value_field('Название ОС'))
        os_name_list.append(get_value_field('Изготовитель системы'))
        os_code_list.append(get_value_field('Код продукта'))
        os_type_list.append(get_value_field('Тип системы'))
        # Преобразуем данные к нужному виду
        main_data = [LIST_GET_FIELDS, *zip(os_prod_list, os_name_list, os_code_list, os_type_list)]
    return main_data if main_data else None


def write_to_csv(fpath):
    """
    Запись данных в файл csv
    :param fpath: полное имя создаваемого файла
    """
    data = get_data()
    if not data:
        return 'Данные не были получены'
    with open(fpath, 'w', encoding='utf-8', newline='') as f:
        file_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        file_writer.writerows(data)


write_to_csv('task_1_write.csv')
