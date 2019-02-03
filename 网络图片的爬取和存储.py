import requests
import os

url = 'http://image.ngchina.com.cn/2019/0203/20190203022207376.jpg'
root = '/Users/Eric/Documents/GitHub/Python_Learning/'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功！')
    else:
        print('文件已存在！')
except:
    print('爬取失败')