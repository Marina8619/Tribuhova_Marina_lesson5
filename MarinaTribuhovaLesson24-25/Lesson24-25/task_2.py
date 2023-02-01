#Задание 2 (I). Выполнить тестирование классов из задания 3 урока 16
#Для всех задач выполняла coverage run -m unittest .\название файла  или coverage -m pytest .\название файла и
#coverage report -m
import unittest
from unittest.mock import Mock


class Bird:
    def __init__(self, name):
        self._name = name

    def fly(self):
        return f"Bird {self._name} flies"

    def walk(self):
        return f"Bird {self._name} walks!"


class FlyingBird(Bird):
    def __init__(self, name, ration="seed"):
        super().__init__(name)
        self._ration = ration


class NonflyingBird:
    def __init__(self, name, ration='seed'):
        self._name = name
        self._ration = ration

    def walk(self):
        return f"Bird {self._name} walks!"


class SuperBird(NonflyingBird, FlyingBird):
    def __init__(self, name, ration):
        super().__init__(name, ration)

    def get_name(self):
        return self._name()

    def swim(self):
        return f"Birn {self._name} swims!"

    def eat(self):
        return f"Bird {self._name} eats {self._ration}!"


class TestBird(unittest.TestCase):

    def setUp(self) -> None:
        self.bird1 = Bird("titmouse")

    def test_fly(self):
        str1 = "Bird titmouse flies"
        self.assertEqual(self.bird1.fly(), str1)

    @unittest.mock.patch('task_2.Bird.walk')
    def test_walk(self, mocked_walk):
        self.bird1.walk()
        self.assertTrue(mocked_walk.called)
        self.bird1.walk()
        self.assertEqual(mocked_walk.call_count, 2)
        mocked_walk.reset_mock()
        self.assertEqual(mocked_walk.call_count, 0)
        self.assertFalse(mocked_walk.called)


class TestFlyingBird(unittest.TestCase):

    def setUp(self) -> None:
        self.bird1 = FlyingBird("bullfinch")

    #проверю наличие наследования
    def test_is_instance(self):
        self.assertIsInstance(self.bird1, Bird)

    def test_fly(self):
        str1 = "Bird bullfinch flies"
        self.assertEqual(self.bird1.fly(), str1)

    @unittest.mock.patch('task_2.FlyingBird.walk')
    def test_walk(self, mocked_walk):
        self.bird1.walk()
        self.assertTrue(mocked_walk.called)
        self.bird1.walk()
        self.assertEqual(mocked_walk.call_count, 2)
        mocked_walk.reset_mock()
        self.assertEqual(mocked_walk.call_count, 0)
        self.assertFalse(mocked_walk.called)


class TestNonflyingBird(unittest.TestCase):

    def setUp(self) -> None:
        self.bird1 = NonflyingBird("ostrich")

    #сравню 2 класса
    def test_two_classes(self):
        self.assertFalse(NonflyingBird == FlyingBird)

    @unittest.mock.patch('task_2.NonflyingBird.walk')
    def test_walk(self, mocked_walk):
        self.bird1.walk()
        self.assertTrue(mocked_walk.called)
        self.bird1.walk()
        self.assertEqual(mocked_walk.call_count, 2)
        mocked_walk.reset_mock()
        self.assertEqual(mocked_walk.call_count, 0)
        self.assertFalse(mocked_walk.called)


class TestSuperBird(unittest.TestCase):

    def setUp(self) -> None:
        self.bird1 = SuperBird("duck", "bread")
        self.bird2 = SuperBird("sparrow", "bread")

    #проверю наличие наследования и сравню 2 класса
    def test_is_instance(self):
        self.assertIsInstance(self.bird1, FlyingBird)
        self.assertFalse(SuperBird == Bird)

    def test_eat(self):
        str1 = "Bird duck eats bread!"
        self.assertEqual(self.bird1.eat(), str1)

    def test_fly(self):
        str1 = "Bird duck flies"
        self.assertEqual(self.bird1.fly(), str1)
        str2 = "Bird sparrow flies"
        self.assertEqual(self.bird2.fly(), str2)

    @unittest.mock.patch('task_2.SuperBird.walk')
    def test_walk(self, mocked_walk):
        self.bird1.walk()
        self.assertTrue(mocked_walk.called)
        self.bird1.walk()
        self.assertEqual(mocked_walk.call_count, 2)
        mocked_walk.reset_mock()
        self.assertEqual(mocked_walk.call_count, 0)
        self.assertFalse(mocked_walk.called)
        self.bird2.walk()
        self.assertTrue(mocked_walk.called)
        self.bird2.walk()
        self.assertEqual(mocked_walk.call_count, 2)
        mocked_walk.reset_mock()
        self.assertEqual(mocked_walk.call_count, 0)
        self.assertFalse(mocked_walk.called)

    @unittest.skipIf(SuperBird.get_name == "sparrow", 'The sparrow can\'t swim')
    def test_swim(self):
        return "The sparrow can\'t swim"



