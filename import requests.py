import requests
req = requests.get("https://www.op.gg/ranking/ladder/")
src = req.content 
from bs4 import BeautifulSoup
soup = BeautifulSoup(src,'lxml')
rank = soup.find('table',{'class':'ranking-table'})
rank2 = rank.find('tbody')
ranks = rank2.find_all('tr')
for a in ranks:
    name = a.find('span')
    print(name.text)
