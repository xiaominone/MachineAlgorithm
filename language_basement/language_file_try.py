# --coding: utf-8 --
#学习文件操作
#  读取文本信息，首先需要读入内存 全部读入or一行一行
#    with 代替close()作用 在不需要访问文件后将文件自动关闭
#    open() 参数是文件相对路径or绝对路径  
#  		open（）返回值表示这个文件的对象  可以用 as 修改名称 存储在as后
#			！！！当使用with, open（）返回的文件对象只能在with代码块内使用
#   1.一次读取全部内容 -> read() 返回一个字符串
import json
with open('language_file_test.txt') as file_obj:
	content = file_obj.read() # content包括字符串内部的空格
print(content.strip())  #strip()删除左右2端空格  字符串内部删除不了
print('-----------------------------')	

#   2.1 在with代码块内部 使用for 一行一行读取  
file_name = 'language_file_test.txt'
with open(file_name) as file_obj:
	for line in file_obj: #每行的末尾都有一个看不见的换行符被读取 
		print(line)
		#print(line.rstrip())    #每一个 print() 都有一个换行
print('-----------------------------')

#   2.2在with代码块外  逐行读取内容 readlines（）返回一个列表 
file_name = 'language_file_test.txt'
with open(file_name) as file_obj:
	lines = file_obj.readlines() 
number = '' #返回的都是字符串
for line in lines: 
	number += line.strip()#删除每行首尾的空格和换行符
print(float(number))
num = input("check a number in number input it:  ")
      #判读字符串是不是子串
if num in number :
	print(num + ' is in the number')
else:
	print(num + 'is not in the number')
print('-----------------------------')


# 3.写入文件  open()  参数1：文件 参数2：读 r 写 w （会清空原文件）  读和写 r+  附加 a (继续向文件写，不清空) 
write_file = ('language_file_test2.txt') #创建文件
with open(write_file,'a') as file_obj:
	#当写入多行需要添加换行符
	file_obj.write("i lova you\n")
	file_obj.write('i am here! ')
print('-----------------------------')	

#4异常  与try-except-else结合   split（）	
file_name  = 'language_file_test2.txt'
try:
	with open(file_name) as file_obj:
		content = file_obj.read()
except FileNotFoundError:
	#当遇到错误，需要忽略时，使用pass
	#pass
	msg = 'Donot have ' + file_name + '!'
	print(msg)
else:
	words = content.split() #split()以空格为分割符，返回列表 
	words_num = len(words)
	print('this files has '+ str(words_num) + ' words')
print('-----------------------------')	

#5.存储数据 实用模块json -> javascriopt_obect_notation
#json.dump() json.load()用法
file_name = 'test_json.json'
words= "adasasasas"
#dump()参数1 存储的数据 参数2 存储的文件对象
with open(file_name,'a') as file_obj:
	json.dump(words,file_obj)
#load（）参数 ->文件对象  返回文件内容
with open(file_name) as f_obj:
	content = json.loads(f_obj)
print(content)


filepath = ''
#统计文件的行数
count = 0
for index, line in enumerate(open(filepath,'r'))： 
    count += 1
