"""
연습문제
다음 뉴스에서 (https://news.daum.net/)
코스피, 코스닥 지수를 찾아주세요.
뉴스 리스트 링크를 리스트에 담아주세요.
뉴스 리스트의 타이틀도 추출해주세요.
추출 후 아래와 같이 출력되게 해주세요. [ { "title" : title , "link" : link } ... ]
"""

import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://news.daum.net/"
res = rq.get(url)
soup = bs(res.text,'html5lib')

# 코스피, 코스닥 지수를 찾아주세요.
kospi = soup.find("div",attrs={"class":"box_side"}).find("div",attrs={"class":"item_kospi"})# 코스피
kosdaq = soup.find("div",attrs={"class":"box_side"}).find("div",attrs={"class":"item_kosdaq"})# 코스닥
# indexs = soup.find_all(attrs={"class":"num_stock"})

print(kospi.find("span",attrs={"class":"num_stock"}))
print(kosdaq.find("span",attrs={"class":"num_stock"}))

# 뉴스 리스트 링크를 리스트에 담아주세요.
news = soup.find("ul",attrs={"class":"list_newsissue"})

type(news.find('a').get('href'))

news_link = list()
for _ in news.find_all('li'):
  item = _.find('a').get('href')
  news_link.append(item)

news_link

# 뉴스 리스트의 타이틀도 추출해주세요. [ { "title" : "link" } ... ]
news = soup.find("ul",attrs={"class":"list_newsissue"})

news_tit = [ _.strong.a.text.strip() for _ in news.find_all('li')] 

news_tit

# 추출 후 아래와 같이 출력되게 해주세요. [ { "title" : title , "link" : link } ... ]
news_link, news_tit

result = [ ({"title" : news_tit[i],
    "link" : news_link[i] }) for i in range(len(news_link))]

# result

# 이메일과 기자명을 추출하여 
# 위의 news_link, news_tit 를 사용하여
# 4가지 출력하는 dict 만들기

# 이메일 추출
res = rq.get(result[0].get('link'))
text = res.text

import re
p = re.compile("\w+@\w+.\w+")
# search 메소드 활용
tmp = p.search(text)
tmp.group()

# 기자 추출
re.search(r"\w+ 기자", text).group()

# dict 만들기

try:
  for i in range(len(result)):
    res = rq.get(result[i].get('link')) # link
    text = res.text
    email = re.search("\w+@\w+.\w+", text).group()
    writer = re.search(r"\w+ 기자", text).group()
    result[i]['email'] = email
    result[i]['writer'] = writer
except AttributeError as e:
  pass

print(result)