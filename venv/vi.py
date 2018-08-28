# sum = 0
# last = 1
# for a in range(1,21):
#
#
# 	b = last * a
# 	# b 是算后的数  b 等于上一次的阶乘 * a
# 	sum = sum + b
#
# 	last = b
#
# print(sum)














# i = input("qing shu ru zhen shu i: ")
# n = int(i)
# if n <= 10:
# 	sum = 0.1 * n
# 	print(sum)
# elif 10 < n < 20:
# 	sum = (n - 10) * 7.5 + 10 * 0.1
# 	print(sum)
# elif 20 <= n < 40:
# 	sum = (n - 10) * 7.5 + 10 * 0.1 + (n - 20) * 0.05
# 	print(sum)
# elif 40 <= n < 60:
# 	sum = (n - 10) * 7.5 + 10 * 0.1 + (n - 20) * 0.05 + (n - 40) * 0.03
# 	print(sum)
# elif 60 <= n < 100:
# 	sum = (n - 10) * 7.5 + 10 * 0.1 + (n - 20) * 0.05 + (n - 40) * 0.03 + (n - 60) * 0.015
# 	print(sum)
# else:
# 	sum = (n - 10) * 7.5 + 10 * 0.1 + (n - 20) * 0.05 + (n - 40) * 0.03 + (n - 60) * 0.015 + (n - 100) * 0.01
# 	print(sum)


# for a in range(100,1000):
# 	b = a % 10
# 	# print(b)
#
# 	c = a // 10 % 10
# 	# print(c)
#
# 	d = a // 100
# 	# print(d)
#
# 	num = b * b * b + c * c * c + d * d * d
# 	if a == num:
# 		print("这个数是水仙花数"+str(num))
# 	# else:
# 		# print("这个数不是水仙花数"+str(num))


n = input("qing shu ru yi ge shu: ")
num = int(n)

surplus = 10
divisor = 1

sum = 0
while True:
	# num %10/1
	last_one = num % 10
	# //surplus // divisor
	sum = sum + last_one
	num = num/10

	if num == 0:
		break

# while True:
# 	# num %10/1
# 	last_one = num % surplus // divisor
#
# 	if last_one == 0:
# 		break
#
# 	sum = sum + last_one
#
# 	surplus = surplus * 10
# 	divisor = divisor * 10
#
#
#
# print(sum)
# l = []
#
# addSum = 0
#
# for n in range(1, 10001):
#     for a in range(1, n):
#         if n % a == 0:
#             l.append(a)
# 			# addSum+= a
# 	# if addSum == n
#     if sum(l) == n:
#         print(l)
#         print(n)
#     l = []