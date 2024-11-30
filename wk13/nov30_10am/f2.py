import threading

"""
Create t1
    ask user for age, then outputs age to screen

Create t2
    Ask user for name, outputs name 5 times to screen

"""
def task1():
    age = int(input("Enter age: "))
    print(f"You are {age} years old")

def task2():
    name = input("Enter your name: ")
    print(f"{name} " * 5)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
# int("abc")
print("Finished!")
