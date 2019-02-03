import requests

url_b = "http://www.baidu.com/s"
url_3 = "http://www.so.com/s"
keyword = "Python"

try:
    kv = {'wd':keyword}
    r = requests.get(url_b, params=kv)
    print(r.request.url)
    r.raise_for_status
    print(len(r.text))
    print('百度关键字爬取成功！')
except:
    print('百度关键字爬取失败！')

try:
    kv = {'q':keyword}
    r = requests.get(url_3, params=kv)
    print(r.request.url)
    r.raise_for_status
    print(len(r.text))
    print('360关键字爬取成功！')
except:
    print('360关键字爬取失败！')