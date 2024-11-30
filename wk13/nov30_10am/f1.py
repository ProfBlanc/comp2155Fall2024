"""
A thread is a process that accomplishes tasks
    a program       =>      task

Every program creates 1 thread to startup the app
    main thread
        may call other threads


"""

import threading

t1 = threading.Thread()
t2 = threading.Thread()

t1.start()
t2.start()
"""

apply/accepted           first step      create thread   

taking classes           start programming  thread running

graduated                  end of program  thread stops running


born                    create thread

running                 thread is running

waiting
            time-waiting        time.sleep(specific time)
blocked
            input statements that don't allow you to 
            continue program execution
dead                    thread finished

"""
import time
print("Started")
print("Waiting for 2 seconds")
time.sleep(2)
print("End of 2-second wait")
input("State of blocked: ")
print("Finished executing")
