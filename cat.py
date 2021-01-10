import requests
req = requests.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4")
src = req.content 
from bs4 import BeautifulSoup
soup = BeautifulSoup(src,'lxml')
cat1 = soup.find('div',{'class':'photowall _photoGridWrapper'})          
cat2 = cat1.find('div',{'class':'photo_grid _box'})
cat3 = cat2.find_all('div',{'class':'img_area _item'})
# cnt = 0                                            / 이미지를 받아줄 벨류?
# for a in cat3:                                     / cat3에 있는 걸 뽑아옴                            
#      cat4 = a.find('a',{'class':'thumb _thumb'})   / 어트리뷰트,어트리뷰트명 아래 있는 것들을 가져옴                      
#      cat5 = cat4.find('img')                                              
#      img_url = cat5['data-source']                 / cat5에 있는 이미지링크? 를 img_url 변수에 넣음 

#      req = requests.get(img_url)                   / 리퀘스트를 통해 이미지링크에 있는 데이터를 받음 
#      f = open("img\\" + str(cnt) + ".png", 'wb')   / 파일을 생성 지금 현재있는 경로에 cnt.png와 를 저장 하겠다 , wb(write byte)로 앞 경로에있는 파일을 씀 
#      f.write(req.content)                          / 파일을 씀
#      f.close()                                     / 파일닫음 (파일저장)
#      cnt += 1                                      / cnt에 1를 더해서 다음 파일은 1.png - 2.png 이렇게 간다 
     
