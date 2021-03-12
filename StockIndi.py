import requests
from bs4 import BeautifulSoup





url = "https://finance.naver.com/sise/sise_market_sum.nhn"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

StockTop50Corp = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("a",attrs={"class":"title"})

for index, Stock in enumerate(StockTop50Corp):
    link = "https://finance.naver.com/" + Stock["href"]

    SubRes = requests.get(link)
    SubSoup = BeautifulSoup(SubRes.text, "lxml")

def getDataOfParam(param):
    SubTbody = SubSoup.find("table", attrs={"class": "tb_type1 tb_num tb_type1_ifrs"}).find("tbody")
    SubTitle = SubTbody.find("th", attrs={"class": param}).get_text().strip()

    DataOfParam = SubTbody.find("th", attrs={"class": param}).parent.find_all("td")

    ValueParam = [i.get_text().strip() for i in getDataOfParam]
    print(SubTitle, ":", ValueParam)
    return ValueParam

    ParamList = ["매출액", "영업이익", "당기순이익", "ROE(지배주주)", "PER(배)","PBR(배)"]
    for idx, pText in enumerate(ParamList):
        param = "".join(SubSoup.find("strong", text=pText).parent["class"])
        getDataOfParam(param)










