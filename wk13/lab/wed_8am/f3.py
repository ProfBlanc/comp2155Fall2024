"""

Create a BankAccount class
    1 private property
        _balance
    2 methods
        withdraw(amount)
            wait for 1 second before withdrawing amount
            raise exception IFF amount exceeds balance
            substracts from balance

        deposit(amount)
            adds to _balance
"""
import time
import threading


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.__lock = threading.Condition()
    def withdraw(self, amount):
        self.__lock.acquire()
        if amount <= self.__balance:
            time.sleep(1)
            self.__balance -= amount
            self.__lock.release()
            return

        self.__lock.release()
        raise ValueError("Amount exceeds balance")

    def deposit(self, amount):
        self.__lock.acquire()
        time.sleep(1)
        self.__balance += amount
        self.__lock.release()

    @property
    def balance(self):
        return self.__balance
# Step 1) Create a BankAccount object with starting balance of 1K
# Step 2) Using threads (threading) withdraw 500 and 700 dollars
# Step 3) Get current balance & note what you observe

account = BankAccount(1000)
t1 = threading.Thread(target=account.withdraw, args=(500,))
t2 = threading.Thread(target=account.withdraw, args=(700,))
t1.start()
t2.start()
time.sleep(1)
print(account.balance)

"""
Make this BankAccount class Thread Safe
Step 1) Add a private property to indicate that a transactions is currently being processes
        threading.Lock              deadlock
        threading.Condition         more methods such as notify, wait,     

Step 2)
        In your withdrawal method, ensure that the transaction is locked before
        withdrawing
        remove lock when finished

"""