import requests as rq
from bs4 import BeautifulSoup as bs

r=rq.get('https://zh-yue.wikipedia.org/wiki/%E9%98%BF%E9%81%93%E5%A4%AB%C2%B7%E5%B8%8C%E7%89%B9%E6%8B%89'
         ,headers={'user-agent':
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})

soup=bs(r.content)

for ty in [f'h{i}' for i in range(7)]+['p']:
    print(ty)
    tx=soup.find_all(ty)
    for i in tx:
 	   print(i.get_text())
     
print(soup.select("a.mw-jump-link"))
print(soup.select('div#mw-teleport-target'))