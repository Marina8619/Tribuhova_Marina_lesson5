# Задание 1
#
# Создайте функцию по вычислению факториала числа. Запустите несколько задач,
# используя ThreadPoolExecutor и замерьте скорость их выполнения, а затем замерьте
# скорость вычисления, используя тот же самый набор задач на ProcessPoolExecutor.
# В качестве примеров, используйте крайние значения, начиная от минимальных и заканчивая
# максимально возможными, чтобы увидеть прирост или потерю производительности.
# Изменить код используя библиотеку asyncio

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


#факториал с функцией генератора

def fact(n):
    mult = 1
    for i in range(1, n + 1):
        mult = mult * i
    yield mult


def threadpool_1():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(factorial, i) for i in range(1, 1001)]
        results = [f.result() for f in futures]
    return results


def threadpool_2():
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(factorial, i) for i in range(1, 1001)]
        results = [f.result() for f in futures]
    return results


def processpool_1():
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(factorial, i) for i in range(1, 1001)]
        results = [f.result() for f in futures]
    return results


def processpool_2():
    with ProcessPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(factorial, i) for i in range(1, 1001)]
        results = [f.result() for f in futures]
    return results

#для проверки экономится ли время передам в пул факториал с функцией генератора


def threadpool_3():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(fact, i) for i in range(1, 1001)]
        results = [f.result() for f in futures]
    return results


def threadpool_4():
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(fact, i) for i in range(1, 1001)]
        results = [f.result() for f in futures]
    return results


def main():
    start = time.time()
    threadpool_1()
    print("ThreadPoolExecutor consisting 2 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    threadpool_2()
    print("ThreadPoolExecutor consisting 50 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    processpool_1()
    print("ProcessPoolExecutor consisting 2 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    processpool_2()
    print("ProcessPoolExecutor consisting 50 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    threadpool_3()
    print("ThreadPoolExecutor with function generator consisting 2 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    threadpool_4()
    print("ThreadPoolExecutor with function generator consisting 50 tasks per pool was completed in ", \
          time.time() - start, "seconds")


if __name__ == '__main__':
    main()






