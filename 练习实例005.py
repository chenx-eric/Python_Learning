# Python 练习实例005
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input('请输入第一个整数：'))
y = int(input('请输入第二个整数：'))
z = int(input('请输入第三个整数：'))
nums = [x,y,z]
# nums.sort()
s_nums = sorted(nums, reverse = False)
print(s_nums)