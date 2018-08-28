# i = 0
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#                 if (x!=y) and (y!=z) and (z!=x):
#                     i += 1
#                     if i%4:
#                         print("%d%d%d" % (x, y, z), end=" | ")
#                     else:
#                         print("%d%d%d" % (x, y, z))

# d = []
# x, y, z = input(" ").split()
#
# a = int(x)
# b = int(y)
# c = int(z)
# if a > b > c:
# dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
# y = int(dat[0:4])  #获取年份
# m = int(dat[5:7])  #获取月份
# d = int(dat[8:])  #获取日
#
# ly = False
#
# if y%100 == 0:  #若年份能被100整除
# 	if y%400 == 0:  #且能被400整除
# 		ly = True  #则是闰年
# 	else:
# 		ly = False
# elif y%4 == 0:  #其它情况下，若能被4整除
# 	ly = True  #则为闰年
# else:
# 	ly = False
#
# if ly == True:  #若为闰年，则2月份有29天
# 	ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# else:
# 	ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# days = 0
# for i in range(1, 13):  #从1到12逐一判断，以确定月份
# 	if i == m:
# 		for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
# 			days += ms[j]
# 		print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案

# q,r,t = input("请输入3个正整数：").split()
# a = int(q)
# b = int(r)
# c = int(t)

# d = []
#
# if a > b:
#
# 	if b > c:
# 		d.append(a)
# 		d.append(b)
# 		d.append(c)
# 		print(d)
# 	else:
# 		d.append(a)
# 		d.append(c)
# 		d.append(b)
# 		print(d)
# elif a < b:
# 	if a > c:
# 		d.append(b)
# 		d.append(a)
# 		d.append(c)
# 	else:
# 		d.append(b)
# 		d.append(c)
# 		d.append(a)
#
# count = 0
# num = 0
#
# d = [1,2,3,4]
#
# for j in d:
# 	for k in d:
# 		for m in d:
# 			if m != j and k!= m and j != k:
# 				num = j*100 + k*10 + m
# 				print("this number is :{}",num)
# 				count += 1
#
# print("All number is :{}",count)


