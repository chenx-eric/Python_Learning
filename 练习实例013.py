# Python练习实例013
# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

def is_narcissistic(number):
    n = list(str(number))
    if number == int(n[0])**3 + int(n[1])**3 + int(n[2])**3:
        return True
    else:
        return False

for i in range(100,1000):
    if is_narcissistic(i):
        print(i, end = '')