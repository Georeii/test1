import time
from threading import Thread
from datetime import datetime


def get_thread(thread_name):
    time.sleep(1)
    print(f"поток {thread_name}")


t1 = datetime.now()
for i in range(1,6):
    get_thread(i)
print("време последоватеьной работы",datetime.now() - t1 )

t2 = datetime.now()
threads = [Thread(target=get_thread, args=(i + 1,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
print("време паралельной работы",datetime.now() - t2 )


