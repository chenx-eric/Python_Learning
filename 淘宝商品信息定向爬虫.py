import requests
import re

def getHTMLText(url, proxies, kv):
    try:
        r = requests.get(url, proxies = proxies, headers = kv, timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("getHTMLText错误")

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("parsePage错误")

def printGoodsList(ilt):
    tplt = "{:^4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = 'QSFP28-100G'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    kv = {'cookie':'lzstat_uv=16385502771690030170|2857556; miid=8845628328567235171; tg=0; cna=39SlD23Ye1ECAdJPTau2yFHy; enc=Rfc55QzNvuAm2desKXitFPd8hJC0HYM5OJXDEXVhgzqzk7JfuAsigqGI1Gr1b14wFmIfur0EIVuaOOAdY%2Buo1Q%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; v=0; t=f6ea7ad0b547b7f489a933bc0a62f661; cookie2=12a8bfc606be5ee18c73e48ab5fa6f39; _tb_token_=51daeeee0a851; unb=512403670; sg=c0e; _l_g_=Ug%3D%3D; skt=d0d5e450375ea787; cookie1=VW9NzYXeIz7Lg8azsYAvki5I0mBoJ3clluZs9lAXFcI%3D; csg=77d50e72; uc3=vt3=F8dByE0Mv4fbkeRMfsw%3D&id2=Vv8bIv9JudgU&nk2=AHLS8Y%2FWx0dFWA%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU0OTUxODUyNg%3D%3D; tracknick=chenx_eric; lgc=chenx_eric; _cc_=WqG3DMC9EA%3D%3D; dnk=chenx_eric; _nk_=chenx_eric; cookie17=Vv8bIv9JudgU; l=AmlpQadRR/IsGGuTUaKJWziR-R7DCF1o; mt=ci=0_1; uc1=cookie14=UoTYP6jUnCNOyA%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=VT5L2FSpczFp&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; isg=BN_f56U5_836VvvRpl8lnDH8bjXWKjPmVycddnEsdw7VAP-CeRTDNl3Wx5B-3wte', \
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
    proxies = {'https:':'https://121.227.76.129'}
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url, proxies, kv)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()