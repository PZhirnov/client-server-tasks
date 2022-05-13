# Задача 1.2
"""
Каждое из слов «class», «function», «method» записать в байтовом типе.
Сделать это необходимо в автоматическом, а не ручном режиме, с помощью добавления литеры b к текстовому значению,
(т.е. ни в коем случае не используя методы encode, decode или функцию bytes) и определить тип, содержимое и длину
соответствующих переменных.
"""


def get_info_in_bites(word):
    word_in_bites = eval(f'b"{word}"')
    print(word_in_bites)
    print(type(word_in_bites))
    print(len(word_in_bites))


# Проверка по условию задачи
get_info_in_bites('class')
get_info_in_bites('function')
get_info_in_bites('method')
