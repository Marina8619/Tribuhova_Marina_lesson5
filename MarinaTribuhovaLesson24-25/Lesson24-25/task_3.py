#Задание 3 (I). Выполнить тестирование класса HistoryDict из задания 3 урока 17.
import unittest


# Задание 3 (I). Реализовать пользовательский словарь (в виде класса), который будет запоминать
# 10 последних измененных ключей. Используя метод "get_history" вернуть эти ключи. Подумайте
# какой подход здесь лучше использовать.
# d = HistoryDict({"foo": 42})
# d.set_value("bar", 43)
# d.get_history()
# >>> ["bar"]

#!!! наследование от класса dict
class HistoryDict(dict):
    def __init__(self, dict1):
        self.__dict1 = dict1
        #использую лист для сохранения упорядоченности ключей, т.к. словарь не упорядоченный
        self.__lst = list(self.__dict1.keys())

    def get_dict(self):
        return self.__dict1

    def get_lst(self):
        return self.__lst

    def set_value(self, key1, value1):
        self.__dict1[key1] = value1
        self.__lst.append(key1)

    def get_history(self):
        return self.__lst[-10:]


class TestHistoryDict(unittest.TestCase):

    def setUp(self) -> None:
        self.d1 = HistoryDict({"foo": 42})

    def test_set_value(self):
        self.d1.set_value("bar1", 43)
        self.assertEqual(self.d1.get_dict(), {"foo": 42, "bar1": 43})

    def test_get_history(self):
        self.d1.set_value("bar1", 43)
        self.d1.set_value("bar2", 44)
        self.d1.set_value("bar3", 45)
        self.d1.set_value("bar4", 46)
        self.d1.set_value("bar5", 47)
        self.d1.set_value("bar6", 48)
        self.d1.set_value("bar7", 49)
        self.d1.set_value("bar8", 50)
        self.d1.set_value("bar9", 51)
        self.d1.set_value("bar10", 52)
        self.d1.set_value("bar11", 53)
        self.d1.set_value("bar12", 53)
        self.assertTrue(self.d1.get_history() == ["bar3", "bar4", "bar5", "bar6", "bar7", "bar8", "bar9", "bar10", \
                                                  "bar11", "bar12"])


