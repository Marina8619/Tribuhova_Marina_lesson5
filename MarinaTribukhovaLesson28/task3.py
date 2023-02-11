# Задание 3 (I). Для таблицы «материала» из задания 2 создайте пользовательскую функцию,
# которая выводит среднюю арифметическую из всех весов таблицы. Подсказка – функция AVG из
# языка SQL

import sqlite3


def avg_weight(db):
    with sqlite3.connect(db) as conn:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        avg_w = cursor.execute("""
        SELECT AVG(weight) FROM materials
        """).fetchone()[0]
        return avg_w


print(avg_weight('materials.sqlite3'))
