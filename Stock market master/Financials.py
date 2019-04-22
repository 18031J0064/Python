import os
import re
import pymysql
import requests
from bs4 import BeautifulSoup
page=requests.get('https://finance.yahoo.com/trending-tickers')
soup=BeautifulSoup(page.text,'html.parser')
db=pymysql.connect("localhost","root","root","ticker")
cursor=db.cursor()

f=open("tickers.txt",'r')
a1=[]
a=f.read()
k=0
a1=a.split("\n")
l=[]
am=[]
for i in range(0,6):
    l = a1[i].split(":")
    path = "C:/Users/user/PycharmProjects/Stock market master/" + l[0] + '/financials.html'
    path1 = "https://finance.yahoo.com/quote/"+l[0]+"/financials?p="+l[0]
    #print(path1)
    req1 = requests.get(path1)
    soup1=BeautifulSoup(req1.text,'html5lib')

    b1=BeautifulSoup(str(soup1.find_all(class_="Fz(s) H(35px) Va(m)")),'html.parser')
    r = b1.find('td')
    s1 = r.get_text()
    print(s1.lstrip())
    b2=BeautifulSoup(str(soup1.find_all(class_='Lh(1.7) W(100%) M(0)')),'html.parser')
    rev=b2.find_all('span')

    for p in range(0,len(rev)):
        a2=rev[p]
        x1=""
        if a2.text=='Total Revenue':
            x1=rev[p+1]
            print(a2.text,x1.text)
            x21=x1.text
        if a2.text == 'Cost of Revenue':
            x2 = rev[p + 1]
            print(a2.text, x2.text)
            x22= x2.text
        if a2.text=='Income Before Tax':
            x3 = rev[p + 1]
            print(a2.text, x3.text)
            x23= x3.text

    b3=soup1.find_all('td', {"class": 'Fw(600) Py(8px) Pt(36px)'})
    b4 = soup1.find_all('td', {"class": 'Fw(600) Ta(end) Py(8px) Pt(36px)'})
    for i, j in zip(b3, b4):
         a4 = i.span.text
         a5 = j.text
         a6=a5.lstrip()
         print("net income",a6)
    sql = "INSERT INTO Finances(FIN_TICKER,TOTAL_REVENUE,COST_OF_REVENUE,INCOME_BEFORE_TAX,NET_INCOME) VALUES(%s,%s,%s,%s,%s)"
    val = (l[0],x21,x22,x23,a6)
    cursor.execute(sql,val)
    k+=1
    if(k==6):
        break
db.commit()

