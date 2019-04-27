# Python 练习实例011
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

def main_rabbit(month):
    x,y,z = 1,1,1
    for i in range(month):
        if i == 0 or i == 1:
            z = 1
        else:
            z = x + y
            x = y
            y = z
    return z

def main():
    for month_index in range(20):
        if month_index == 0:
            pass
        else:
            print('第{}个月的兔子总数为{}对。'.format(month_index, main_rabbit(month_index)), end = '')

main()