import os
import re
import pymysql
import requests
from bs4 import BeautifulSoup
page=requests.get('https://finance.yahoo.com/trending-tickers')
soup=BeautifulSoup(page.text,'html.parser')
db=pymysql.connect("localhost","root","root","ticker")
cursor=db.cursor()
k=0
f=open("tickers.txt",'r')
a1=[]
l1=0
a=f.read()
a1=a.split("\n")
l=[]
income_str=""
s=0
sno=0
for i in range(0,6):
    l = a1[i].split(":")
    sno+=1
    #print(l[0])
    path = 'C:/Users/user/PycharmProjects/Stock market master/' + l[0] + '/statistics.html'
    path1 = "https://finance.yahoo.com/quote/" + l[0] + "/key-statistics?p=" + l[0]

    #print(path1)
    req1 = requests.get(path1)
    soup1 = BeautifulSoup(req1.text, 'html5lib')
    b1=BeautifulSoup(str(soup1.find_all(class_="table-qsp-stats Mt(10px)")),'html.parser')
    #print(b1)
    rev = b1.find_all('table')
    tables = b1.find_all('table')
    for i in range(len(tables)):
        mytabl = tables[i]
        tds = mytabl.findAll('td')
        for j in range(0,len(tds),2):
            if (tds[j].text == 'Market Cap (intraday) 5') or (tds[j].text == 'Enterprise Value 3') or (tds[j].text == 'Return on Assets (ttm)') or (tds[j].text == 'Total Cash (mrq)') or (tds[j].text == 'Operating Cash Flow (ttm)') or (tds[j].text == 'Operating Cash Flow (ttm)') or (tds[j].text == 'Levered Free Cash Flow (ttm)') or (tds[j].text == 'Total Debt (mrq)') or (tds[j].text == 'Current Ratio (mrq)') or (tds[j].text == 'Profit Margin ') or (tds[j].text == 'Gross Profit (ttm)') :
                print(tds[j].text + " : " + tds[j + 1].text)
                x31=tds[j + 1].text
    sql = "INSERT INTO Statistics(SNO,STAT_TICKER,MARKETCAP,ENTERPRISE_VALUE,RETURN_ON_ASSESTS,GROSS_PROFIT,TOTAL_CASH,TOTAL_DEBT,CURRENT_RATIO,OPERATING_CASH_FLOW,LEVERED_FREE_CASH_FLOW,PROFIT_MARGIN) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (sno,l[0],x31,x31,x31,x31,x31,x31,x31,x31,x31,x31)
    cursor.execute(sql, val)
    k += 1
    if (k == 6):
        break
db.commit()
