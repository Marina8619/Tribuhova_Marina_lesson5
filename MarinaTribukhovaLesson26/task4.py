#Задание 4 (I). Имеется файл data.csv, (можно взять любые данные и конвертировать их в csv
#(см. ссылку ниже)) содержащий информацию в csv-формате. Напишите функцию read_csv()
#для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя
#первую строку как имена ключей, а каждую последующую строку как значения этих ключей.
#Функция read_csv() не должна принимать аргументов


import csv

#создаю новый диалект, т.к. csv класс у меня с разделителем |
class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_MINIMAL
    delimiter = "|"
    quotechar = " "
    escapechar='\\'
    strict = False
    lineterminator = "\n"
# регистрация диалекта
csv.register_dialect("marina_dialect", dialect=MyDialect)

def read_csv():
    with open('data/data.csv') as f:
        lst = []
        # Преобразует строки csv в словарь
        reader = csv.DictReader(f, dialect=MyDialect)
        for row in reader:
            lst.append(row)
    return lst


print(read_csv())



