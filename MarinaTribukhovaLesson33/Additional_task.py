# Дополнительные задания
#
# Используя ThreadPoolExecutor выполнить серию запрсов на различные страницы
# Википедии и определить статус страницы: если возвращаемый статус код == 200,
# то статус == страница существует, если код 400, то - страница не существует.
# В списке должно быть не менее 5 url-ов. измерьте время выполнения кода без ThreadPoolExecutor и с ним

import requests
import concurrent.futures
import time

urls = [
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/JJJ',
    'https://en.wikipedia.org/wiki/Java_(programming_language)',
    'https://en.wikipedia.org/wiki/PHP',
    'https://en.wikipedia.org/wiki/C_Sharp_(programming_language)',
]


def check_existence(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} - страница существует")
    elif response.status_code == 404:
        print(f"{url} - страница не существует")
    else:
        print(f"{url} - ошибка {response.status_code}")

# без использования ThreadPoolExecutor
start_time = time.time()
for url in urls:
    check_existence(url)
print(f"Время выполнения без ThreadPoolExecutor: {time.time() - start_time}")

# с использованием ThreadPoolExecutor
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(check_existence, urls)
print(f"Время выполнения с ThreadPoolExecutor: {time.time() - start_time}")
