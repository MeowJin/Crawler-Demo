import requests
from bs4 import BeautifulSoup

url="https://www.baidu.com/s?wd=%E6%9E%97%E4%BF%8A%E6%9D%B0&rsv_spt=1&rsv_iqid=0xd97108f2006ca3b9&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=11&rsv_sug2=0&rsv_btype=i&inputT=1393&rsv_sug4=3359"

response=requests.get(url)

# print(response)

# html='''
# <title>爬虫</title>
# <body>
#     <h1>标题</h1>
#     <h2>标题2</h2>
#     <p>段落
# '''

html=response.text

soup=BeautifulSoup(html, "lxml")

# print(soup)

# ps=soup.find_all(name="h1")
content_all=soup.find_all("div")
for content in content_all:
    print(content.string)


