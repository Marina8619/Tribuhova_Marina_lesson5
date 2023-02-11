# Задание 4 (II). Используя модуль sqlite3, реализуйте реальное добавление пользователей в
# базу. Должны быть реализовать следующие функции и классы:
#  класс пользователя, содержащий в себе следующие методы: get_full_name (ФИО с
# разделением через пробел: «Петров Игорь Сергеевич»), get_short_name (ФИО формата:
# «Петров И. С.»), get_age (возвращает возраст пользователя, используя поле birthday типа
# datetime.date); метод __str__ (возвращает ФИО и дату рождения).
#  функция регистрации нового пользователя (принимаем экземпляр нового пользователя и
# отправляем Email на почту пользователя с благодарственным письмом).
#  функция отправки Email с благодарственным письмом (эмитируем отправку).
#  функция поиска пользователей в таблице users по имени, фамилии и почте

import sqlite3
from datetime import datetime, date


class User:
    def __init__(self, last_name, first_name, patronymic, birthday, email):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birthday = birthday
        self.email = email

    def get_full_name(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.patronymic)

    def get_short_name(self):
        return "{} {}. {}.".format(self.last_name, self.first_name[0], self.patronymic[0])

    def get_age(self):
        date_today = datetime.now().date()
        age = date_today.year - self.birthday.year - ((date_today.month, date_today.day) < (self.birthday.month, \
                                                                                            self.birthday.day))
        return age

    def __str__(self):
        return "{} {}".format(self.get_full_name(), self.birthday)


def register_new_user(user):
    with sqlite3.connect("users.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (last_name, first_name, patronymic, birthday, email)")

        cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)", (user.last_name, user.first_name, user.patronymic, \
                                                              user.birthday, user.email))
        conn.commit()
        send_email(user.email)
        cursor.close()


def send_email(email):
    print(f"Thank you for your registration with your email {email}!\n\t\t\t\t\t\t\tUser Support Service")


def find_user(first_name, last_name, email):
    with sqlite3.connect("users.sqlite3") as conn:
        cursor = conn.cursor()
        user_find = cursor.execute("SELECT * FROM users WHERE first_name=? AND last_name=? AND email=?", \
                   (first_name, last_name, email)).fetchall()
        if user_find:
            print(f"Search results {user_find}")
        else:
            print("There is no such user in the database!!!")




Marina = User("Tribukhova", "Marina", "Aleksandrovna", date(1986, 5, 20), "m_marine_f@mail.ru")
register_new_user(Marina)
print(Marina.__str__())
print(Marina.get_age())
print(Marina.get_short_name())
print(Marina.get_full_name())
find_user('Marina', 'Tribukhova', 'm_marine_f@mail.ru')
find_user('Elena', 'Tribukhova', 'm_marine_f@mail.ru')
