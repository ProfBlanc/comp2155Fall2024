"""

A thread is a PROCESS that has own resources

    worker


To create a Thread

    Step 1:
        import the module
            ???
                threading

"""

import threading


t1 = threading.Thread()
t1.start()

# every program create 1 thread
    # the name of the thread is 99% of the time
    # a four letter word?
    # almost every city/county has a street name that
    # shares this same four-letter word
    # main


mt = threading.current_thread()

print(mt.name)
print(t1.name)  # Thread-1
t2 = threading.Thread()
print(t2.name)

"""
thread cycle very similar to a life cycle
    
    born        when thread created
    
    running     when thread started
                meaning it starts the tasks assigned
    
    
    time-waiting
                    time.sleep   
                    waiting for specific amount of time
                    
    blocked         input request 
    
    
    dead        when thread finishes all its tasks


"""
age = input("What is your name? ")

# t1.run()  # run tasks on current thread

