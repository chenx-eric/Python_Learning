# Python 练习实例002
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
# 超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# 方式一
i = int(input('\n请输入利润(单位:万元)：'))
r = 0
if i < 10:
    r = i*0.1
elif i <= 20:
    r = 10*0.1 + (i - 10)*0.075
elif i <= 40:
    r = 10*0.1 + 10*0.075 + (i - 20)*0.05
elif i <= 60:
    r = 10*0.1 + 10*0.075 + 20*0.05 + (i - 40)*0.03
elif i <= 100:
    r = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + (i - 60)*0.015
elif i > 100:
    r = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + 40*0.015 + (i - 100)*0.01

print('\n应获得提成{:.2f}万元\n'.format(r))

# 方式二
profit = int(input('\n请输入利润总额(单位：万元)：'))
bonus_level = [100, 60, 40, 20, 10, 0]
bonus_point = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for index in range(len(bonus_level)):
    if profit > bonus_level[index]:
        bonus = bonus + (profit - bonus_level[index])*bonus_point[index]
        profit = bonus_level[index]
print('\n提成总额为{:.2f}万元\n'.format(bonus))