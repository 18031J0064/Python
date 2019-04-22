import requests
import os
from bs4 import BeautifulSoup
page=requests.get('https://finance.yahoo.com/trending-tickers')
soup=BeautifulSoup(page.text,'html.parser')
f=open('tickers.txt',"r")
l=f.read()
l1=l.split("\n")
i=0
for line in range(0,6):
    #print(l1[line])
    str = l1[line].split(":")
    dirname = str[0]
    # check directory exists
    if (os.path.exists('C:/Users/user/PycharmProjects/Stock market master/' + str[0])):
        i += 1
        pass
    else:
        os.mkdir('C:/Users/user/PycharmProjects/Stock market master/' + str[0])
        print(str[0])
        i += 1
        tk = str[0]

        path = 'C:/Users/user/PycharmProjects/Stock market master/' + tk + '/statistics.html'
        f1 = open(path, 'w')
        append = "https://finance.yahoo.com/quote/" + tk + "/key-statistics?p=" + tk
        req1 = requests.get(append)
        soup1 = BeautifulSoup(req1.content, 'html5lib')
        try:
            f1.write(soup1.prettify())
        except Exception as e:
            pass

        path = 'C:/Users/user/PycharmProjects/Stock market master/' + tk + '/summary.html'
        f2 = open(path, 'w')
        append = "https://finance.yahoo.com/quote/" + tk + "/?p=" + tk
        req1 = requests.get(append)
        soup1 = BeautifulSoup(req1.content, 'html5lib')
        try:
            f2.write(soup1.prettify())
        except Exception as e:
            pass

        path = 'C:/Users/user/PycharmProjects/Stock market master/' + tk + '/profile.html'
        f3 = open(path, 'w')
        append = "https://finance.yahoo.com/quote/" + tk + "/profile?p=" + tk
        req1 = requests.get(append)
        soup1 = BeautifulSoup(req1.content, 'html5lib')
        try:
            f3.write(soup1.prettify())
        except Exception as e:
            pass

        path = 'C:/Users/user/PycharmProjects/Stock market master/' + tk + '/financials.html'
        f4 = open(path, 'w')
        append = "https://finance.yahoo.com/quote/" + tk + "/financials?p=" + tk
        req1 = requests.get(append)
        soup1 = BeautifulSoup(req1.content, 'html5lib')
        try:
            f4.write(soup1.prettify())
        except Exception as e:
            pass

    if (i == 6):
        break

