import requests
from bs4 import *
import matplotlib.pyplot as plt

page = requests.get("https://mfd.ru/currency/?currency=USD")
soup = BeautifulSoup(page.text, "html.parser")

chet = 1
usd_graf = []
data_graf = []
for j in soup.find_all("table", class_="mfd-table mfd-currency-table"):
    for link in j.find_all('tr'):
        # print(link)
        for i in link.find_all('td'):
            if chet > 3 :
                chet = 1
            if chet % 2 == 0:
                usd_graf.append(i.get_text())
            elif chet // 2 == 0 and chet // 3 == 0:
                data_graf.append(i.get_text())
            chet +=1

plt.plot(data_graf,usd_graf,'ro')
plt.show()





