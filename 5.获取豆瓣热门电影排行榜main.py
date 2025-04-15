import urllib.request
import urllib.parse
import json

# https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=0&limit=20&category=%E6%9C%80%E6%96%B0&type=%E5%85%A8%E9%83%A8

def create_request( page ):
    base_url = 'https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?'

    parameter = {
        'start': (page-1)*20,
        'limit': 20,
        'category': '热门',
        'type': '全部'
    }

    parm = urllib.parse.urlencode(parameter)

    url = base_url + parm

    headers = {
        'Referer': 'https://m.douban.com/',
        'Host': 'm.douban.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    return content

def save_data(content, page):
    try:
        # 将JSON字符串转为Python对象
        data = json.loads(content)
        # 保存解码后的中文
        with open(f"douban_{page}.json", 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")


if __name__=='__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))

    for page in range(start_page , end_page+1):
        request = create_request(page)
        content = get_content(request)
        save_data(content, page)