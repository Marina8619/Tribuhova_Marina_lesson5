# Задание 2 (I). Создайте таблицу «материалы» из следующих полей: идентификатор, вес, высота
# и доп. характеристики материала. Поле доп. характеристики материала должно хранить в себе
# массив, каждый элемент которого является кортежем из двух значений, первое – название
# характеристики, а второе – её значение. Пример, "[('wheels', 4), ('passengers', 5)]"

import sqlite3

try:
    connection = sqlite3.connect('materials.sqlite3')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE materials (id, weight, height, characteristic)')
    cursor.execute("""
    INSERT INTO materials(id, weight, height, characteristic)
    VALUES (1, 30, 40, "[('name', 'steel'), ('density', 7850)]"),
           (2, 20, 50, "[('name', 'granite'), ('density', 2700)]"),
           (3, 50, 40, "[('name', 'limestone'), ('density', 2400)]")
    """)
    row = cursor.execute(
        """
        SELECT * FROM materials 
        """).fetchall()
    print(row)
    connection.commit()
    cursor.close()
except sqlite3.Error as error:
    print("Failed to read data from table", error)
finally:
    if connection:
        connection.close()
        print("The Sqlite connection is closed")




