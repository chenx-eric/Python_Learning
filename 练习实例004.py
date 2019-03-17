# Python 练习实例004
# 题目：输入某年某月某日，判断这一天是这一年的第几天？

date = input('\n请输入您要查询的日期(以YYYYMMDD格式输入)：')
nonlp_year = [31,28,31,30,31,30,31,31,30,31,30,31]
lp_year = [31,29,31,30,31,30,31,31,30,31,30,31]
status = True
days = 0

if len(date) == 8:
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])
    if month < 1 or month > 12:                                         # 判断月份
        status = False
    if day < 1 or day > 31:                                             # 判断日期
        status = False
    if day > 30 and month in [4,6,9,11]:                                # 判断月份对应天数是否正确
        status = False
    if year % 4 == 0 and month == 2 and day > 29:                       # 判断闰年2月日期
        status = False
    if year % 4 != 0 and month == 2 and day > 28:                       # 判断非闰年2月日期
        status = False    

    if status:
        print('您要查询的日期是{}年{}月{}日'.format(year, month, day))
        if year % 4 == 0:
            for i in range(month - 1):
                days = days + lp_year[i]
        else:
            for i in range(month - 1):
                days = days + nonlp_year[i]
        days = days + day
        print('您查询的这天是这一年的第{}天\n'.format(days))
    else:
        print('您输入的日期有误，请检查！\n')
else:
    print('您输入的日期有误，请检查！\n')