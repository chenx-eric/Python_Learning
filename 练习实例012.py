# Python练习实例012
# 题目：判断101-200之间有多少个素数，并输出所有素数。

from math import sqrt

def is_prime(number):
    for n in range(2, int(sqrt(number))+1):
        if m % n == 0:
            return False
    return True


prime_number = []
for m in range(101,201):
    if(is_prime(m)):
        prime_number.append(m)

print('共有{}个素数，列举如下：'.format(len(prime_number)))
print(prime_number)