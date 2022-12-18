import requests
from bs4 import *
import matplotlib.pyplot as plt

page = requests.get("https://mfd.ru/currency/?currency=USD")
soup = BeautifulSoup(page.text, "html.parser")

chet = 1
chet_sd = 1
s = 0
usd_graf = []
data_graf = []
for j in soup.find_all("table", class_="mfd-table mfd-currency-table"):
    if s != 0:
        break
    for link in j.find_all('tr'):
        # print(link)
        if s != 0:
            break
        for i in link.find_all('td'):
            if chet > 3:
                chet = 1
            if chet_sd == 21:
                s = 1
                break
            if chet % 2 == 0:
                usd_graf.insert(0,float(i.get_text()))
                print(i)
            elif chet ==1:
                data_graf.insert(0,i.get_text())
                print(i)

            chet_sd += 1
            chet += 1


plt.plot(data_graf, usd_graf, 'ro')
plt.show()






