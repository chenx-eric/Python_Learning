# Python 练习实例007
# 题目：将一个列表的数据复制到另一个列表中

def fib(n):                 # 定义斐波那契数列
    fx,fy = 1,1
    for i in range(n-1):
        fx,fy = fy,fx+fy
    return(fy)

a = []
for i in range(10):         # 生成斐波那契列表
    a.append(fib(i))
print(a)

b = a                       # 复制列表
print(b[0])
print(b)