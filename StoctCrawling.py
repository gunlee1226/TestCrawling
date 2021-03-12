import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

StockHead = soup.find("thead").findAll("th")
DateHead = [head.get_text() for head in StockHead]

StockList = soup.find("table", attrs={"class" : "type_2"}).find("tbody").findAll("tr")

print(DateHead)
for Stock in StockList:
    if len(Stock) > 1:
        print(Stock.get_text().split())


