import requests
from bs4 import BeautifulSoup
symbol=[]
name=[]
file=open("tickers.txt","w")
page = requests.get('https://finance.yahoo.com/trending-tickers')
soup = BeautifulSoup(page.text, 'html.parser')
#ticker_table=soup.find(class_='yfinlist-table W(100%) BdB Bdc($tableBorderGray)')
#ticker_symbol=ticker_table.find_all('a')
#ticker_name=soup.find(class_='data-col1 Ta(start) Pstart(10px) Miw(180px)')
ticker_symbol=soup.find_all('td',attrs={"class":"data-col0"})
ticker_name=soup.find_all('td',attrs={"class":"data-col1"})
for k,l in zip(ticker_symbol,ticker_name):
    symbol+=str(k.text).split(' ')
    name+=str(l.text).split('\n')
#print(symbol)
#print(name)
a=len(symbol)
while name.count('')>0:
    name.remove('')
while name.count('\n')>0:
    name.remove('\n')
for i in range(a):
    file.write(symbol[i]+':'+name[i]+'\n')


