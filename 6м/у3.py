import requests
from threading import Thread
from datetime import datetime


def get_html(link):
    res = requests.get('https://scotch.io').text


sait = ["https://brunoyam.getcourse.ru/pl/teach/control/lesson/view?id=203321995",
        "https://brunoyam.getcourse.ru/pl/teach/control/lesson/view?id=203321993",
        "https://brunoyam.getcourse.ru/pl/teach/control/lesson/view?id=203321992",
        "https://brunoyam.getcourse.ru/pl/teach/control/lesson/view?id=211648854",
        "https://brunoyam.getcourse.ru/pl/teach/control/lesson/view?id=203321991"]

threads = [Thread(target=get_html, args=(i,)) for i in sait]

t1 = datetime.now()
for t in sait:
    get_html(t)

print("време последоватеьной работы",datetime.now() - t1)

t2 = datetime.now()
for e in threads:
    e.start()
for e in threads:
    e.join()
print("време последоватеьной работы",datetime.now() - t2 )
