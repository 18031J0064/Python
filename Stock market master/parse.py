import os
import re
import pymysql
import requests
from bs4 import BeautifulSoup
page=requests.get('https://finance.yahoo.com/trending-tickers')
soup=BeautifulSoup(page.text,'html.parser')
db=pymysql.connect("localhost","root","root","ticker")
cursor=db.cursor()

v=0
f=open("tickers.txt",'r')
a1=[]
l=[]
a=f.read()
a1=a.split("\n")
for i in range(0,6):
    v+=1
    l=a1[i].split(":")
    path=("C:/Users/user/PycharmProjects/Stock market master/" + l[0]+"profile.html")

    f1=open(path,'w')
    path1 = "https://finance.yahoo.com/quote/" + l[0] + "/profile?p=" + l[0]
    req1 = requests.get(path1)
    soup1=BeautifulSoup(req1.text,'html5lib')

    #name
    soup3 = BeautifulSoup(str(soup1.find_all(class_="Mt(15px)")), 'html.parser')
    name=soup3.find('h1')
    s=name.get_text()
    print(s)

    # retrieving data from html page:address
    soup2 = BeautifulSoup(str(soup1.find_all(class_="D(ib) W(47.727%) Pend(40px)")), 'html.parser')
    add = soup2.get_text().strip("[]")
    address = re.sub(r'http\S+', '', add)
    print(address)

    # retrieving data from html page:Website
    emd = BeautifulSoup(str(soup1.find_all(class_="D(ib) W(47.727%) Pend(40px)")), 'html.parser')
    emm = emd.get_text().strip("[]")
    emailid = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', emm)
    email = str(emailid).strip("[],''")
    print(email)

    # phone num
    soup2 = BeautifulSoup(str(soup1.find_all(class_="asset-profile-container")), 'html.parser')
    add = soup2.find('p')
    ph = soup2.find('a')
    z = ph.get_text()
    print(z)

    #getting sector,industry,fulltime employees
    sector=soup1.find_all('span')
    for i in range(0,len(sector)):
        y1=sector[i]
        if y1.text=='Sector':
            x1=sector[i+1]
            x2=sector[i+3]
            x3=sector[i+5]
            print(x1.text,"\n",x2.text,"\n",x3.text,"\n")

    # database
    sql = "INSERT INTO Profiles(PROF_TICKER,NAME,ADDRESS,PHONENUM,WEBSITE,SECTOR,INDUSTRY,FULL_TIME) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (l[0],s, address,z,email,x1.text,x2.text,x3.text)
    cursor.execute(sql, val)
    if v==6:
        break

db.commit()




