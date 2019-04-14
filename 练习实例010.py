# Python 练习实例010
# 题目：暂停一秒输出，并格式化当前时间

import time

print('')
while(True):
    print('\r{}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())), end = '')
    time.sleep(1)