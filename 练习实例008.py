# Python 练习实例008
# 题目：输出 9*9 乘法口诀表。

i = [1,2,3,4,5,6,7,8,9]
j = 1
while(j < 10):
    for index in range(j):
        print('{}*{}={}\t'.format(i[index],j,j*i[index]), end = '')
    print('\n')
    j = j + 1