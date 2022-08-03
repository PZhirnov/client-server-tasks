# Задачи 2-3. Обе задачи решены в одном скрипте
import platform
from ipaddress import ip_address, ip_interface
from subprocess import Popen, PIPE
from threading import Thread
import chardet
from itertools import zip_longest
from tabulate import tabulate


# ----- Задание 2. Функция для пингования диапазона ip адресов (включает диалог с пользователем)
def host_range_ping(num_pings: int = 2):
    """
    Функция включает диалог по условиям задачи.
    Пингование хостов делается в потоках.
    :param num_pings: количество пингов, которые необходимо выполнить для каждого хоста
    :return: словарь возвращает два списка
    """
    # общие параметры

    # список списков для результатов - Reachable и Unreachable
    RESULTS = {
        "reachable": [],
        "unreachable": [],
    }
    PARAM = '-n' if platform.system().lower() == 'windows' else '-c'
    threads = []  # список для потоков

    # диалог ввода первоначального ip адреса
    while True:
        first_ip = None
        first_ip_input = input('Введите первоначальный ip адрес:')
        try:
            first_ip = ip_address(first_ip_input)
        except ValueError:
            print('Введен некорректный ip адрес!')
        if first_ip:
            break
    # ввод проверяемого дипазона адресов - меняется только последений октет
    while True:
        try:
            range_ping = int(input('Сколько адресов проверить? :'))
            if 1 <= range_ping <= 256:
                break
            else:
                raise ValueError
        except ValueError:
            print('Необходимо ввести число от 1 до 256!')

    def worker_thread(ip_host):
        ip = ip_address(ip_host)
        args = ['ping', PARAM, str(num_pings), str(ip)]
        reply = Popen(args, shell=True, stdout=PIPE)
        code = reply.wait()
        reachable = True if code == 0 else False
        #  --- Если хост в локальной сети, то в ответе должно быть
        # более 2 значений пингуемого ip, если хост доступен ---
        reply_text = reply.stdout.read()
        encoding = chardet.detect(reply_text).get('encoding', None)
        reply_text = reply_text.decode(encoding)
        check_number_ip = reply_text.count(str(ip)) > 2
        # добавляем результат проверки в список
        if reachable and check_number_ip:
            RESULTS['reachable'].append(ip)
        else:
            RESULTS['unreachable'].append(ip)

    # если все было введено корректно, то получаем генератор
    hosts_range_gen = ip_interface(f'{first_ip}/24').network.hosts()
    # создаем потоки для проверяемых хостов
    i = 0  # счетчик для выхода из цикла после проверки заданного диапазона
    for host in hosts_range_gen:
        t = Thread(target=worker_thread, args=(host,))
        threads.append(t)
        t.start()
        i += 1
        if i == range_ping:
            break
    # ждем завершения работы всех потоков
    [thread.join() for thread in threads]
    return RESULTS

# print(host_range_ping())


#  ----- Задание 3. Представление результата в табличном формате
def host_range_ping_tab(results_dict):
    """
    Функция получает словарь со списками из фнукции host_range_ping() и формирует таблицу.
    :param results_dict: словарь со списками 'reachable' и 'unreachable'
    :return: таблица c результатами
    """
    # В список кортежей передадим первую строку, которая будет заголовком
    tuples_list = [
        ("Reachable", "Unreachable"),
    ]
    # Получим результаты пингования и добавим в итоговый список
    tuples_results = list(zip_longest(results_dict['reachable'],
                                      results_dict['unreachable']))
    tuples_list.extend(tuples_results)
    return tabulate(tuples_list, headers='firstrow', tablefmt="pipe")


# Проверка результата
print(host_range_ping_tab(host_range_ping()))


"""
Тест: 1
Введите первоначальный ip адрес:8.8.8.8
Сколько адресов проверить? :10
| Reachable   | Unreachable   |
|:------------|:--------------|
| 8.8.8.8     | 8.8.8.6       |
|             | 8.8.8.10      |
|             | 8.8.8.7       |
|             | 8.8.8.9       |
|             | 8.8.8.5       |
|             | 8.8.8.1       |
|             | 8.8.8.4       |
|             | 8.8.8.2       |
|             | 8.8.8.3       |

"""
