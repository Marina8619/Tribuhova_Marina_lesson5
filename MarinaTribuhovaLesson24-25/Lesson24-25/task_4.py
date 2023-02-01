#Задание 4 (I). Выполнить тестирование для классов из задания 4 урока 18
import unittest



# Задание 4 (II). Реализовать класс Material, который представляет однородный материал
# (вещество). Атрибуты класса name и density являются приватными. Метод get_material()
# должен возвращать строку, разделенную «;»
# Output:
# steel;7850.0
# Создать класс Subject, который представляет объект, состоящий из однородного материала.
# Атрибуты класса: name, material, volume (объем) должны быть приватными. Реализовать
# методы класса get_mass() (приватный), который возвращает массу объекта
# (=density*volume) и get_subject(), который возвращает строку со всеми атрибутами (плюс
# масса (mass)), разделенную «;»
# Output:
# wire;steel;7850.0;0.03;235.5
# Определите класс Runner (інтерфейс для управления внутренними классами), где:
# 1. Создайте объект, представляющий стальную проволоку (steel_wire) объемом 0,03 м3.
# 2. Вывести содержимое объекта на консоль, используя метод get_subject().
# 3. Обновите материал проволоки на медь (copper) (плотность = 8500.0 и выведите его массу).
# Output:
# The wire mass is 255.0 kg
# В этой задаче нет отношения наследования между сущностями (материал и предмет).
# Наследование возникает, когда одна сущность является частным случаем другой. Например,
# металл (или другое твердое вещество) и материал. Другими словами, металл является
# материалом. Предмет состоит из материала, а не является материалом. Поэтому предмет не может
# быть наследником от материала.
# Обратите внимание, что у конкретного материала плотность является константой, что нужно
# отразить при создании класса. Например, у стали плотность 7850.0 и никакая другая.


class Material:

    def __init__(self, name):
        materials = {"steel": 7850.0, "copper": 8500}
        self.__name = name
        self.__density = materials[self.__name]

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_density(self):
        return self.__density

    def get_material(self):
        return self.__name + ";" + str(self.__density)


class Subject:

    def __init__(self, name, material, volume):
        self.__name = name
        self.__material = material.get_name()
        self.__volume = volume
        self.__density = material.get_density()

    def __get_mass(self):
        mass = self.__density * self.__volume
        return mass

    def get_subject(self):
        return self.__name + ";" + self.__material + ";" + str(self.__density) + ";" + str(self.__volume) + \
               ";" + str(self.__get_mass())

    def get_density(self):
        return self.__density

    def get_volume(self):
        return self.__volume


class Runner:
    def __init__(self, name, material):
        self.__name = name
        self.__material = Material(material)
        self.__subject = Subject(self.__name, self.__material, 0.03)

    def get_name(self):
        return self.__name

    def get_subject(self):
        return self.__subject.get_subject()

    def set_material(self, material):
        self.__material = Material(material)
        self.__subject = Subject(self.get_name(), self.__material, 0.03)

    def get_material(self):
        return self.__material

    def get_mass(self):
        mass = self.__subject.get_density() * self.__subject.get_volume()
        return f"The {self.__name} mass is {mass} kg"


class TestMaterial(unittest.TestCase):
    def setUp(self) -> None:
        self.material1 = Material("steel")

    def test_get_name(self):
        self.assertTrue(self.material1.get_name() == "steel")

    def test_density(self):
        self.assertEqual(self.material1.get_density(), 7850)

    def test_get_material(self):
        self.assertEqual(self.material1.get_material(), 'steel;7850.0')
        self.assertFalse(self.material1.get_material() == 'copper";8500')

    def test_is_instance(self):
        self.assertIsInstance(self.material1, Material)

    @unittest.skipIf(Material.get_name != ("steel", "copper"), 'The material is not specified correctly')
    def test_get_name_not_correct(self):
        return "The material is not specified correctly"


class TestSubject(unittest.TestCase):

    def setUp(self) -> None:
        self.subject1 = Subject("wire", Material("steel"), 0.03)

    def test_get_subject(self):
        self.assertEqual(self.subject1.get_subject(), 'wire;steel;7850.0;0.03;235.5')

    def test_get_density(self):
        self.assertEqual(self.subject1.get_density(), 7850)

    def test_get_volume(self):
        self.assertFalse(self.subject1.get_volume() == 0.0003)
        self.assertTrue(self.subject1.get_volume() == 0.03)


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.runner1 = Runner("wire", "steel")

    def test_get_name(self):
        self.assertEqual(self.runner1.get_name(), "wire")

    def test_get_subject(self):
        self.assertEqual(self.runner1.get_subject(), "wire;steel;7850.0;0.03;235.5")

    def test_get_material(self):
        self.assertFalse(self.runner1.get_material() == "copper")

    def test_get_mass(self):
        mass = 7850.0 * 0.03
        self.assertEqual(self.runner1.get_mass(), f'The wire mass is {mass} kg')







