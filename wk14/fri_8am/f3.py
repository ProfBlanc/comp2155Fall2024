"""
Create a BankAccount class
    private attribute: balance
    public methods
        deposit(amount)
        withdraw(amount)
            raise exception if amount is greater than balance
            wait randomly between .5-1.5 seconds
"""
import random
import threading
import time


class BankAccount:
    def __init__(self, balance):
        self.__balance = max(0, balance)
        self.__lock = threading.Condition()
        # if balance < 0: self.__balance = 0
        # else: self.__balance = balance
    def deposit(self, amount):
        self.__lock.acquire()
        time.sleep(random.randint(250, 1500) / 100)
        self.__balance += amount
        self.__lock.release()
    def withdraw(self, amount):
        self.__lock.acquire()
        if amount > self.__balance:
            self.__lock.release()
            raise ValueError("Insufficient funds")
        time.sleep(1)
        self.__balance -= amount
        self.__lock.release()

    @property
    def balance(self):
        return self.__balance

account = BankAccount(1000)
deposits = [500, 700]
for deposit in deposits:
    threading.Thread(target=account.withdraw, args=(deposit,)).start()
time.sleep(1)
print(account.balance)


# account.withdraw(500)
# account.withdraw(700)
# print(account.balance)
