import urllib.request
import urllib.parse
import  json

# get请求

# url= "https://www.baidu.com/s?"
#
# parameter={
#     'wd': '成毅',
#     'sex': '男'
# }
#
# headers={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# }
#
# parm = urllib.parse.urlencode(parameter)
#
# url+= parm
#
# print(url)
#
# request=urllib.request.Request(url=url, headers=headers)
#
# response= urllib.request.urlopen(request)
#
# content= response.read().decode('utf-8')
#
# print(content)

# post请求
url= "https://fanyi.baidu.com/sug"

data={
    'kw': '蜘蛛'
}

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

data = urllib.parse.urlencode(data).encode('utf-8')

# post请求参数必须编码
request=urllib.request.Request(url=url, data=data, headers=headers)

response= urllib.request.urlopen(request)

content= response.read().decode('utf-8')

obj= json.loads(content)

print(obj)

