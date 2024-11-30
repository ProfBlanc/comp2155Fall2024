"""
Create a new thread that ask user to input age
    output age to console

Create a new thread that ask user to input name
    output name 5 times to screen. all on one line

"""
# print(__name__)

def task1():
    age = int(input("Enter your age: "))
    print(age)

def task2():
    name = input("Enter your name")
    print(f"{name} " * 5)

import threading
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# how many threads are BORN at this line? THREE
# how many threads are RUNNING? ONE ??? main

t1.start()
t2.start()
int("abc")
print("End of program! Goodnight!")

# Fun Activity: Start t2() first and see the resultts
# note your observations

