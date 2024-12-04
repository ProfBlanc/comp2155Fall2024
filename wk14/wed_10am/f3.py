"""

creating a BankAccount class
    1 private property
        balance
    2 public methods
        withdraw(amount)
            determine if amount is less than or equal to balance
                YES: withdraw amount and update balance
                        delay the withdrawal process by 1 second
                NO: raise a ValueError exception

        deposit
    1 public property accessor
        access the private balance property


"""
import threading
import time
import random


class BankAccount:
    def __init__(self, balance):
        self.__balance = max(0, balance)
        self.__lock = threading.Condition()
    @property
    def balance(self): return self.__balance
    def deposit(self, amount):
        with self.__lock:
            time.sleep(1)
            self.__balance += amount
    def withdraw(self, amount):
        self.__lock.acquire()
        if amount > self.__balance:
            self.__lock.release()
            raise ValueError("Amount is greater than balance")
        time.sleep(random.randint(250, 1251)/1000)
        self.__balance -= amount
        self.__lock.release()

"""
Create a BankAccount object with starting amount of 1000
Using threads
    call the withdraw method of the one and only BankAccount object
    with the amounts of 500 and 700
    make sure that you pause execution for 1 second between each withdraw

Outside of threads, output the balance. Note your observations
"""
account = BankAccount(1000)
amounts = [500, 200]
for amount in amounts:
    threading.Thread(target=account.withdraw, args=(amount,)).start()
time.sleep(1)
print(account.balance)