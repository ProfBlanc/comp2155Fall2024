"""

Create a BankAccount
    private property: balance
        have an accessor
    public method
        deposit(amount)
            pause execution for 1 second
            add amount to balance
        withdraw(amount)
            ensure amount is LTE balance
                raise ValueError
            pause execution before subtracting amount from balance


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
            self.__balance += max(0, amount)
    def withdraw(self, amount):
        self.__lock.acquire()
        if amount > self.__balance:
            self.__lock.release()
            raise ValueError("insufficient funds")
        time.sleep(1)
        self.__balance -= amount
        self.__lock.release()

account = BankAccount(1000)
withdrawals = [500, 600]

# account.withdraw(withdrawals[0])
# account.withdraw(withdrawals[1])
for amount in withdrawals:
    threading.Thread(target=account.withdraw, args=(amount,)).start()
time.sleep(1.5)
print(account.balance)