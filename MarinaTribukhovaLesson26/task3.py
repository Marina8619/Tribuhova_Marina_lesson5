# Задание 3 (I). Поработайте с созданием собственных диалектов, произвольно выбирая правила
# для CSV файлов. Зарегистрируйте созданные диалекты и поработайте, используя их, с
# созданием/чтением файлом

import csv

# создание собственного диалекта для записи файла в csv через класс

class MarinaDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "@"
    quotechar = "~"
    lineterminator = "\n\n"

# регистрация диалекта
csv.register_dialect("marina_dialect", dialect=MarinaDialect)

with open('data/output1_task3.csv', 'w') as file:
    # Два варианта передачи диалекта: 1) через имя диалекта при регистрации
    # 2) через имя класса
    writer = csv.writer(file, dialect='marina_dialect')
    writer.writerow([1, 2, 3, 4])
    writer.writerow(["one", "two", "three", "four"])
    writer.writerow([11, 12, 13, 14])
    writer.writerow(["eleven", "twelve", "thirteen", "fourteen"])
# Открываем файл на чтение
with open('data/output1_task3.csv', "r") as file:
    reader = csv.reader(file)
    print("Lines num", reader.line_num)
    print("Dialect", reader.dialect) # Диалект устанавливает правила парсинга файла

    #Считываем файл построчно
    for row in reader:
        print("Lines num", reader.line_num)
        print(row)

# создание собственного диалекта для записи файла в csv через класс

class TribukhovaDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "|"
    quotechar = "%"
    lineterminator = "\n"

# регистрация диалекта
csv.register_dialect("tribukhova_dialect", dialect=TribukhovaDialect)

with open('data/output2_task3.csv', 'w') as file:
    writer = csv.writer(file, dialect=TribukhovaDialect)
    writer.writerow(['A', 'B', 'C', 'D'])
    writer.writerow(['E', 'F', 'G', 'H'])
    writer.writerow(['I', 'J', 'K', 'L'])
    writer.writerow(['M', 'N', 'O', 'P'])
    writer.writerow(['Q', 'R', 'S', 'T'])
    writer.writerow(['U', 'V', 'W', 'X'])
    writer.writerow(['Y', 'Z'])

# Открываем файл на чтение
with open('data/output2_task3.csv', "r") as file:
    reader = csv.reader(file)
    print("Lines num", reader.line_num)
    print("Dialect", reader.dialect) # Диалект устанавливает правила парсинга файла

    #Считываем файл построчно
    for row in reader:
        print("Lines num", reader.line_num)
        print(row)
