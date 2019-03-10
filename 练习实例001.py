# Python 练习实例001
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

num = [1, 2, 3, 4]
for i in range(len(num)):
    a = num[i]
    for j in range(len(num)):
        b = num[j]
        for k in range(len(num)):
            c = num[k]
            if (a!=b and a!=c and b!=c):
                print('{}{}{}'.format(a, b, c))