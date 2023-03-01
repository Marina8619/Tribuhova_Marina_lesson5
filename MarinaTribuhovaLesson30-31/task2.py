# Задание 2. Создайте три функции, одна из которых читает файл на диске с заданным именем и
# проверяет наличие строку “Wow!”. В случае, если файла нет, то засыпает на 5 секунд, а затем
# снова продолжает поиск по файлу. В случае, если файл есть, то открывает его и ищет строку
# “Wow!”. При наличии данной строки закрывает файл и генерирует событие, а другая функция
# ожидает данное событие и в случае его возникновения выполняет удаление этого файла. В случае
# если строки «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и
# проверьте выполнение программы

import time
import os
import threading


def find_word(file_name: str):
    while True:
        if not os.path.exists(file_name):
            time.sleep(5)
            # create_file('my_file.txt.txt')
        else:
            with open(file_name, 'r') as file:
                if file.read().find('Wow!'):
                    event.set()
                    #поток освободится для следующего потока с удалением файла
                    event.clear()
                    break
                else:
                    time.sleep(5)


#файл вручную создала
def create_file(file_name: str):
    with open(file_name, 'a') as file:
        file.write('This is the file created by Marina Tribukhova!\n Today is the first day of spring!\n \
                   Wow!\n Good bye!!!')


def delete_file(file_name: str):
    event.wait()
    os.remove(file_name)


event = threading.Event()


thread1 = threading.Thread(target=find_word, args=('my_file.txt',))
thread2 = threading.Thread(target=delete_file, args=('my_file.txt',))


thread1.start()
thread2.start()

thread1.join()
thread2.join()