"""
Задание №3
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
1. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого
ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
2. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также
установить возможность работы с юникодом: allow_unicode = True;
3 - 4. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

# 1. Словарь по условию задачи
DATA_TEST = {
    "φ": ['hello', 'привет', '֍ ֍ ֍ ֍ ֍'],
    "©§¥": 777,
    "¾½¼": {
        (1, 2): 'один',
        2: 'два',
        'три': '3'
    },
}

FILE_NAME = 'file.yaml'
print(DATA_TEST)


# 2. Запись данных
def save_yaml(data, file_name):
    """
    Функция сохраняет данные словаря в файл yaml
    :param data: словарь
    :param file_name: имя создаваемого файла
    :return:
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


# 3. Чтение данных
def load_yaml(file_name):
    """
    Функция для чтения данных из файла YAML
    :param file_name: имя файла
    :return: содержимое файла в виде словаря
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        f_to_dict = yaml.load(f, Loader=yaml.FullLoader)
    return f_to_dict


# ------ Проверка решения ------
save_yaml(DATA_TEST, FILE_NAME)
result_load = load_yaml(FILE_NAME)
print(DATA_TEST)
print(result_load)

# 4. Проверка результатов
print(result_load == DATA_TEST)  # должно быть True
