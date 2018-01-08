# --coding: utf-8 --
# 异常,一种管理程序执行期间出错的特殊对象  发生异常，告诉程序怎样继续执行
#  try-except       try-except-else
try:
	print(5/0)  #没有出现错误执行try,有错误执行except中指定的错误
except ZeroDivisionError: #指定错误
	print('You can not divide by zero')
print('-----------------------------')

print("input q is ending!")
while True:
	a = input("input a: ")
	b = input("input b: ")
	if a == 'q' or b == 'q':
		break;
	try:
		c = float(a)/float(b)
	except ZeroDivisionError:
		print('You can not set b = 0')
		#2. pass 告诉python遇到这种错误置之不理  
	else:#依赖于try代码块可以成功执行的代码放到else中
		print('a/b=' + str(c))
print('-----------------------------')


	
