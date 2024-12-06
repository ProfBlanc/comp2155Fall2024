"""

Create a BankAccount class
    1 private attribute
        balance
    1 getter for balance, but no setter
    2 methods
        deposit(amount)
            pause for 1 second
            add amount to the balance
        withdraw(amount)
            ensure amount is LTE to balance
                YES: withdraw money
                NO: raise ValueError

"""
import threading
import time


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
            raise ValueError(f"insufficient funds. "
                             f"You only have ${self.__balance} "
                             f"in your account, and cannot withdraw ${amount}")
        time.sleep(1)
        self.__balance -= amount
        self.__lock.release()


account = BankAccount(1000)
# account.withdraw(500)
# account.withdraw(700)

for amount in range(5, 7):
    threading.Thread(target=account.withdraw, args=(amount * 100,)).start()
time.sleep(1)
print(account.balance)
