import pandas as pd
import requests
def get_special():
    print("=======爬取专业数据==========")
    num = 0
    for i in range(1, 182):
        num = num + 1
        address = "http://yz.kaoyan365.cn/zhuanye/list_0_0_0_0_" + str(i) + ".html"
        html_data = requests.get(address)
        html_table_data = pd.read_html(html_data.content)
        html_table_data[0].to_csv("../data_csv/专业数据-中公.csv", mode='a', header=False,
                                  index=False)
        data = 20 * num
        print("已爬取{}条数据,{}%".format(data, round(i * 100 / 181, 2)))
    print("=======专业数据爬取完成==========")

def get_schoolline():
    print("=======爬取分数线数据==========")
    num = 0
    # 循环爬取7398页的分数线数据
    for i in range(1, 7399):
        try:
            num = num + 1
            # 拼接网址
            address = "http://yz.kaoyan365.cn/fenshuxian/list_0_0_0_0_" + str(i) + ".html"
            # 获取网页数据
            html_data = requests.get(address)
            # 使用pandas将html表格转换为DataFrame
            html_table_data = pd.read_html(html_data.content)
            # 将DataFrame保存为CSV文件
            html_table_data[0].to_csv("../data_csv/分数线数据-中公.csv", mode='a',
                                      header=False, index=False)
            # 计算已经爬取的数据条数和进度百分比
            data = 10 * num
            progress = round(i * 100 / 7398, 2)
            # 打印已爬取的数据条数和进度百分比
            print("已爬取{}条数据,{}%".format(data, progress))
        except Exception as e:
            print("第{}页出现异常: {}".format(i, e))
    print("=======分数线数据爬取完成==========")

def get_rate():
    print("=======爬取报录比数据==========")
    num = 0
    for i in range(1, 5550):
        try:
            num = num + 1
            # 拼接网址
            address = "http://yz.kaoyan365.cn/baolubi/list_0_0_0_" + str(i) + ".html"
            # 获取网页数据
            html_data = requests.get(address)
            # 使用pandas将html表格转换为DataFrame
            html_table_data = pd.read_html(html_data.content)
            # 将DataFrame保存为CSV文件
            html_table_data[0].to_csv("../data_csv/报录比数据-中公.csv", mode='a',
                                      header=False, index=False)
            # 计算已经爬取的数据条数和进度百分比
            data = 20 * num
            progress = round(i * 100 / 5549, 2)
            # 打印已爬取的数据条数和进度百分比
            print("已爬取{}条数据,{}%".format(data, progress))
        except Exception as e:
            print("第{}页出现异常: {}".format(i, e))
    print("=======报录比数据爬取完成==========")


if __name__ == "__main__":
    # get_rate()          #爬取报录比数据
    # get_schoolline()    #爬取分数线数据
    get_special()         #爬取专业数据


