# import requests     
# req = requests.get("https://www.op.gg/ranking/ladder/")
# src = req.content 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(src,'lxml')

# rank1 = soup.find('div',{'class':'Content'})              ('div',{'class':'Content'}) 밑에 있는걸 다 가져옴
# rank2 = rank1.find('div',{'class':'ranking-highest'})     ('div',{'class':'ranking-highest'}) 밑에 있는걸 다 가져옴 
# rank3 = rank2.find('ul')                                   ul 밑에있는거 다가져옴 
# rank4 = rank3.find_all('li')                               li밑에있는거 다 가져옴 
# b = 0                                                       --위 를 쓰기 위한 변수 를 만듬 
# for a in rank4:                                             rank4에 있는걸 a로 순서대로 빼옴 
#     name = a.find('a',{'class':'ranking-highest__name'})    
#     b = b+1                                                변수 b에다 1을 증감시킴 
#     print (str(b)+'위 ' +name.text)                         정수인 b을 문자열로 바꿔주고 문자열 '위'를 넣고 파싱한 name을 넣음 


# ranking = soup.find('tbody') 
# ranking2 = ranking.find_all('tr')
# b = 5                                                     1~5위는 이미 있으므로 5부터 시작함
# for a in ranking2:
#     name2 = a.find('span') 
#     b = b+1
#     print(str(b)+'위' + name2.text)   

b = input('number:')
for a range(int(b)):
    c  = 0 
    c = c+b
print(c)





