#爬取院校信息：https://yz.chsi.com.cn/sch/（研招网）

import requests
from bs4 import BeautifulSoup
import csv

# 定义空列表来保存获取的信息
info = [["学校名称", "位置", "院校隶属", "是否有研究生院", "是否自划线", "是否双一流", "图标链接", "url"]]

# 循环请求每一页
for k in range(0, 880, 20):
    # 构造请求url
    url = 'https://yz.chsi.com.cn/sch/?start=' + str(k)

    # 发送请求
    response = requests.get(url)

    # 判断请求是否成功
    if response.status_code == 200:
        # 获取网页源码
        html = response.text
    # 解析网页源码
    soup = BeautifulSoup(html, 'html.parser')

    # 找到所有学校的标签
    schools = soup.find_all('div', class_='sch-item')

    # 遍历每一个学校标签
    for school in schools:
        # 获取学校图标url
        icon = school.find('img').get('src')
        # 获取学校链接url
        link = school.find('a', class_='name js-yxk-yxmc text-decoration-none').get('href')
        # 获取学校名称
        name = school.find('a', class_='name').text.strip()
        # 获取学校标签
        if school.find('span', class_='sch-tag'):
            # tag = school.find('span', class_='sch-tag').text.strip()
            tag = 1
        else:
            # tag = ''
            tag = 0

        # 获取学校所在地、隶属、科研方向和自划线标志
        department = school.select_one('.sch-department').get_text().split()
        location = department[0].replace('\ue6a4', '')  # 去除不需要的字符
        depart = department[1].split('：')[-1]

        if len(department) == 3:
            # search = department[2]
            # line = ""
            search = 1
            line = 0

        elif len(department) == 4:
            # search = department[2]
            # line = department[3]
            search = 1
            line = 1

        else:
            # search = ""
            # line = ""
            search = 0
            line = 0
        # 将获取的信息添加到列表中
        info.append([name, location, depart, search, line, tag, icon, link])

        # 显示爬取进度
    print("已爬取{0}%".format(round(k * 100 / 880, 2)))

# 将获取的信息保存到csv文件中
print("==============正在保存数据==================")

with open('../data_csv/研招网院校20230801.csv', 'w', newline='', encoding="UTF-8") as csvfile:
    writer = csv.writer(csvfile)
    for i in info:
        writer.writerow(i)
csvfile.close()

print("==============爬取完成==================")
