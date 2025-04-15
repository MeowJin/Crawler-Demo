import urllib.request

url="http://www.baidu.com"

response= urllib.request.urlopen(url)
# read方法 返回的是字节形式的二进制数据
# 要将二进制数据转换为字符串
# 二进制-->字符串 解码 decode('编码的格式')
content= response.read().decode('utf-8')

print(content)

