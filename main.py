from DrissionPage import ChromiumPage
import json
import csv
import time
import random

# 1.打开浏览器
dp = ChromiumPage()

# 2.访问网站
keyword = 'IT总监'
url = f'https://we.51job.com/pc/search?jobArea=070300&keyword={keyword}&searchType=2&jobType=0&sortType=0&metro='
dp.get(url)

# 创建文件对象
f = open ('data.csv', mode='w', encoding='utf-8', newline='')
fieldnames=['职位', '公司名称', '薪资范围', '城市' , '经验要求' , '学历要求', '领域', '公司性质', '规模' , '标签']
csv_writer = csv.DictWriter(f,fieldnames=fieldnames)
csv_writer.writeheader()

for page in range(1, 51):
    print(f'正在采集第{page}页的数据内容')

    retry_count = 0
    time.sleep(random.uniform(2, 5) * (2 ** retry_count))  # 随机休息几秒钟，防止请求过快

    # 下滑页面  下滑到底部
    dp.scroll.to_bottom()

    # 3.获取数据节点 构建数据
    # 第一次提取:获取所有职位信息所在的div标签
    divs = dp.eles('css:.joblist-item')
    for div in divs:
        info = div.ele('css:.joblist-item-job').attr('sensorsdata')
        data = json.loads(info)
        city = data['jobArea'].split('·')[0]
        cname = div.ele('css:.cname').attr('title')
        cly = div.ele('css:.bl span:nth-child(3)').text if div.ele('css:.bl span:nth-child(3)', timeout=0) else ''
        shrink = div.ele('css:.bl span:nth-child(4)').text if div.ele('css:.bl span:nth-child(4)', timeout=0) else ''
        cgm = div.ele('css:.bl span:nth-child(5)').text if div.ele('css:.bl span:nth-child(5)', timeout=0) else ''

        tags = [i.text for i in div.eles('css:.tag')]
        dit = {
            '职位' : data['jobTitle'],
            '公司名称': cname,
            '薪资范围' : data['jobSalary'],
            '城市' : city,
            '经验要求' : data['jobYear'],
            '学历要求' : data['jobDegree'],
            '领域' : cly,
            '公司性质' : shrink,
            '规模' : cgm,
            '标签' : tags
        }
        print(dit)
        # 写入数据
        csv_writer.writerow(dit)

    # 定位下一页按钮, 进行点击操作
    dp.ele('css:.btn-next').click()





