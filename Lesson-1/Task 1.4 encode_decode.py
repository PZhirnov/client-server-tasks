# Задание 1.4
"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

def get_encode_decode_data(word):
    word_encode = word.encode('utf-8')
    word_decode = word_encode.decode('utf-8')
    return f'{word} --> {word_encode} --> {word_decode}'


# Исходные данные
list_word = ['разработка', 'администрирование', 'protocol', 'standard']
for i in list_word:
    print(get_encode_decode_data(i))
