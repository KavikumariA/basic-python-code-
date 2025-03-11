import threading
import time

def worker(event, name):
    print(f"{name} waiting for event to start with timeout")
    if event.wait(timeout=5):
        print(f"{name} has started working")
    else:
        print(f"{name} timed out waiting for event")

event = threading.Event()
t = threading.Thread(target=worker, args=(event, 'Thread 1'))
t.start()

# Do not set the event
time.sleep(6)
print("Main thread did not set the event")

t.join()