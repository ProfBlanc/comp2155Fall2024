"""
main thread
    main that creates threads
        associates tasks to threads
"""
import threading
print(__name__)
main_thread = threading.current_thread()
print(main_thread.name)

#Thread-N....  where N starts at 1
t1 = threading.Thread()
print(t1.name)

"""
Programs have the same cycle as life as humans

The fact that you are alive and breathing,
that means that your ____ on a specific day
    born
    

BORN/NEW        when thread var created

RUNNING         when thread has started

WAITING         time-waiting. time.sleep()

BLOCKED         waiting for input()

DEAD            when thread finishes tasks/statements 

"""

t1.start()
