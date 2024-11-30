"""
Create a thread that counts from 1 to a specified
number, skipping 3 numbers at a time
Run this thread

Create a thread that ask user for their age,
output their age
Run this thread

Create a thread that ask user for their name
Output their name 3 times
Run this thread
"""
import threading
import time


#Step 1: create a function
#Step 2: create and start thread

def task1(end):
    for i in range(1, end + 1, 3):
        print(i)
def task2():
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
def task3():
    name = input("Enter your name: ")
    print(f"{name} " * 3)

t1 = threading.Thread(target=task1, args=(19,))
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)
t1.start()
t2.start()
t3.start()
