# Python 练习实例006
# 题目：斐波那契数列

f0 = 0
f1 = 1
for i in range(100):
    if i == 0:
        fi = f0
    elif i == 1:
        fi = f1
    else:
        fi = f0 + f1
        f0 = f1
        f1 = fi
    print('{}, '.format(fi), end = '')