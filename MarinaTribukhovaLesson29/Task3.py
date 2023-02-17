# Задание 3 (II). В коде программы из папки Task3 допущена ошибка, вызывающая Deadlock.
# Задача – исправить код так, чтобы программа блокировала потоки

from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.lock = Lock()
#вызов методов acquire() и release(), чтобы только один поток User смог вмешаться в область
    # памяти, когда происходит пополнение счета
    def replenish(self, s=10):
        self.lock.acquire()
        print(self.money, 'money:', self.name)
        self.money += s
        print('Replenish cash:', self.name)
        self.lock.release()

    # вызов методов acquire() и release(), чтобы только один поток User смог вмешаться в область
    # памяти, когда происходит снятие со счета
    def withdraw(self, s=10):
        self.lock.acquire()
        print(self.money, 'money:', self.name)
        sleep(1)
        self.money -= s
        print('Withdraw cash:', self.name)
        self.lock.release()
# закоментировала ошибку, т.к. может вызываться deadlock(2 объекта lock будут работать одновременно),
    # потоки User могут зависать и получим неожиданный результат
    def transfer(self, friend_bank, s=10):
        # with (self.lock, friend_bank.lock):
        print('Lock myself: ', self.name)
        self.withdraw(s)
        print('Lock friend: ', friend_bank.name)
        friend_bank.replenish(s)


class User(Thread):
    def __init__(self, name, bank, friend_bank):
        super().__init__(name=name)
        self.name = name
        self.bank = bank
        self.friend_bank = friend_bank

    def run(self):
        print(f'{self.name} try to transfer to {self.friend_bank.name}')
        self.bank.transfer(self.friend_bank)
        print(f'{self.name} made transfer operation to {self.friend_bank.name}')


bank1 = Bank('Bob')
bank2 = Bank('Kate')
bank3 = Bank('Ann')

user1 = User('Bob', bank1, bank2)
user2 = User('Kate', bank2, bank3)
user3 = User('Ann', bank3, bank2)


user1.start()
user2.start()
user3.start()

user1.join()
user2.join()
user3.join()

print(bank1.money)
print(bank2.money)
print(bank3.money)

#после исправления ошибки с захватом области памяти мы всегда получается ожидемый результат
#90
#110
#100