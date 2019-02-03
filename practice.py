import requests
import time

def getHTMLText(url):
    try:
        for i in range(1,101):
            r = requests.get(url)
            r.raise_for_status() # 如果状态不是200，引发HTTPError异常
            r.encoding = r.apparent_encoding
            print("第{}次爬取百度首页".format(i))
        return r.text
    except:
        return "产生异常"

def main():
    url = "http://www.baidu.com"
    start = time.perf_counter()
    getHTMLText(url)
    end = time.perf_counter()
    print("一共用时{}秒".format(end - start))

main()