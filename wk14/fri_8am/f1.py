import random
import threading
import time


def method(value):
    time.sleep(random.randint(250, 1500)/1000)  # wait b/t 0.25 and 1.5 seconds
    print("Method called with value", value)


t1 = threading.Thread(target=method, args=("value1",))
t2 = threading.Thread(target=method, args=("value2",))
t3 = threading.Thread(target=method, args=("value3",))

t1.start()
t2.start()
t3.start()

print("Finished!")
