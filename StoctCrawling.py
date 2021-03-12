import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

stock_head = soup.find("thead").findAll("th")
data_head = [head.get_text() for head in stock_head]

stock_list = soup.find("table", attrs={"class" : "type_2"}).find("tbody").findAll("tr")

print(data_head)
for stock in stock_list:
    if len(stock) > 1:
        print(stock.get_text().split())

