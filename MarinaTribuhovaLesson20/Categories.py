# Напишите импровизированную БД, содержащую имя сотрудника и категорию (например,
# {"John": "A", "Mike": "B"}) реализуйте интерфейс, через который можно узнать зарплату
# сотрудника по его категории. В программе должно быть два класса Core() и Interface().
# На вход должно подаваться только имя сотрудника.

# Напишите импровизированную БД, содержащую имя сотрудника и категорию (например,
# {"John": "A", "Mike": "B"}) реализуйте интерфейс, через который можно узнать зарплату
# сотрудника по его категории. В программе должно быть два класса Core() и Interface().
# На вход должно подаваться только имя сотрудника.

class Core:

    database_employees = {"John": "A", "Mike": "B", "Sveta": "C", "Ivan": "B"}

    def __init__(self, name):
        #self.__categories_employees = {"John": "A", "Mike": "B", "Sveta": "C", "Ivan": "B"}
        self.__name = name
        self.__category = self.categories_employees(self.__name)
        self.__salary_employees = {"A": 1000, "B": 2000, "C": 3000}

    # @property
    # def categories_employees(self):
    #     return self.__categories_employees

    @classmethod
    def categories_employees(cls, name):
        return cls.database_employees[name]

    @classmethod
    def get_database_employees(cls):
        return cls.database_employees

    def salary_categories(self):
        """
        determines the salary by category
        :param category:
        :return:
        """
        return f"The salary of the employee {self.__name} with a category {self.__category} equal to \
{self.__salary_employees[self.__category]} dollars"


class Interface:
    print("Database of employees of the enterprise!")
    print(Core.get_database_employees())
    name1 = input("Enter the name of the employee to get the category: ")
    employee1 = Core(name1)
    print(employee1.salary_categories())
