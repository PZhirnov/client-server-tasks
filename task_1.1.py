from subprocess import Popen, PIPE
import platform
from ipaddress import ip_address
import socket
from threading import Thread
import chardet


def host_ping(hosts: list, num_pings: int = 2):
    """
    Функция проверяет доступность сетевых узлов.
    :PARAM hosts: список сетевых узлов, представленных именем хоста или ip-адресом
    :PARAM num_pings: количество пингов, которое надо сделать (2 по умолчанию)
    :return: список с результатами проверки
    """
    RESULTS = []  # список для результатов
    PARAM = '-n' if platform.system().lower() == 'windows' else '-c'
    threads = []  # список для потоков

    def worker_thread(host):
        """
        Функция используется для реализации многопоточности и добавляет
        результаты запросов в словарь RESULTS.
        В аргументе host может быть имя хоста или ip адрес.
        Функция учитывает возможность пинговая узлов в локальной сети, где код ответа
        Popen может не корректно интерпретироваться (т.е. будет 0 для несуществующих узлов)
        """
        check_number_ip: int  # используется для проверки количества значений ip в ответе
        ip = ''
        try:
            ip = ip_address(socket.gethostbyname(host))
            reachable = True
        except Exception:
            reachable = False
        if reachable:
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
        RESULTS.append(f"Узел {host} ({ip}) "
                       f"{'доступен' if reachable and check_number_ip else 'недоступен'}!\n")
    # создаем потоки для проверяемых хостов
    for host in hosts:
        t = Thread(target=worker_thread, args=(host,))
        threads.append(t)
        t.start()
    # ждем завершения работы всех потоков
    [thread.join() for thread in threads]
    return RESULTS


# ------- Проверка решения ---------
urls_list = ['8.8.8.8', 'google.com',
             'yandex.ru', 'bbbaaamail.ru', 'mail.ru',
             '192.168.0.155', '192.168.0.140']

print(*host_ping(urls_list), sep='')

'''
Пример результата:
Узел bbbaaamail.ru () недоступен!
Узел yandex.ru (77.88.55.77) доступен!
Узел 8.8.8.8 (8.8.8.8) доступен!
Узел google.com (216.58.210.174) доступен!
Узел 192.168.0.155 (192.168.0.155) доступен!
Узел 192.168.0.140 (192.168.0.140) недоступен!
Узел mail.ru (217.69.139.202) доступен!
'''
