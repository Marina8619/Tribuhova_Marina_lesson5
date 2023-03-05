from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import asyncio


async def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


async def threadpool_1():
    with ThreadPoolExecutor(max_workers=2) as executor:
        # это набор запускаемых задач
        futures = set()
        for i in range(1000):
            task = asyncio.create_task(factorial(i))
            # Добавление задачи в набор создает сильную ссылку.
            futures.add(task)
            # Чтобы не хранить ссылки на завершенные задачи, необходимо
            # продумать, чтобы после завершения каждая задача
            # самостоятельно удаляла свою ссылку из этого набора:
            task.add_done_callback(futures.discard)
        results = await asyncio.gather(*futures)
    return results


async def threadpool_2():
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = set()
        for i in range(1000):
            task = asyncio.create_task(factorial(i))
            futures.add(task)
            task.add_done_callback(futures.discard)
        results = await asyncio.gather(*futures)
    return results


async def processpool_1():
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = set()
        for i in range(1000):
            task = asyncio.create_task(factorial(i))
            futures.add(task)
            task.add_done_callback(futures.discard)
        results = await asyncio.gather(*futures)
    return results


async def processpool_2():
    with ProcessPoolExecutor(max_workers=50) as executor:
        futures = set()
        for i in range(1000):
            task = asyncio.create_task(factorial(i))
            futures.add(task)
            task.add_done_callback(futures.discard)
        results = await asyncio.gather(*futures)
    return results


async def run():
    start = time.time()
    await threadpool_1()
    print("ThreadPoolExecutor consisting 2 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    await threadpool_2()
    print("ThreadPoolExecutor consisting 50 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    await processpool_1()
    print("ProcessPoolExecutor consisting 2 tasks per pool was completed in ", time.time() - start, "seconds")
    start = time.time()
    await processpool_2()
    print("ProcessPoolExecutor consisting 50 tasks per pool was completed in ", time.time() - start, "seconds")

asyncio.run(run())





