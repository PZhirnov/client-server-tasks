# Задача 1.3
"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""


def check_convert(word):
    try:
        word_in_bites = eval(f'b"{word}"')
        return word_in_bites
    except SyntaxError:
        return 'невозможно записать в байтовом виде'


# Исходные данные
data_for_check = ['attribute', 'класс', 'функция', 'type']
for word in data_for_check:
    print(f'{word} - {check_convert(word)}')
