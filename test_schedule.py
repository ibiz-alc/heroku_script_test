from threading import Event, Thread

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

cancel_future_calls = call_repeatedly(5, print, "Hello, World")



# do something else here...
# cancel_future_calls() # stop future calls

# import threading

# def printit():
#   threading.Timer(5.0, printit).start()
#   print("Hello, World!")

# printit()