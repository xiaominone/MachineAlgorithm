# --coding: utf-8 --
from random import randrange 
message = ["Aa",'Bb','Cc','Dd','Ee'];
#1 直接打印列表
print(message)
print('\n')
#2 通过索引输出列表内容（通过内容找索引）（查）
print(message[0].upper())
print(message[-1].title())
print(message.index('Bb'))
print('\n')
#3 修改列表元素 （改）
message[2] = 'Ww'
print(message)
print('\n')
#4 添加列表元素 （增  ２种）
message.append('Ff')
message.append('End')
message.insert(0,'Start')
message.insert(3,'!!')
print(message)
print('\n')
#5 删除列表元素（３种）  分为 1索引删除del与pop 、del 列表.[索引]      列表.pop(索引)
#（pop方法会返回删除的列表元素）
                  #2值删除 remove()，若列表中有相同元素，只能删除第一个指定值
	#del listname[index]  可以先listname.index(内容)获得对应的索引
del message[1]
	#pop默认删除末尾元素，并且返回该元素
message.pop()
	#删除指定位置元素 
delate_yuansu = message.pop(2)
print(delate_yuansu)
message.remove('Bb')
print(message)
print('\n')
#6 排序　　　　列表.sort()　与 sorted(列表)返回排序列表
print(message[::-1]) #切片
message.reverse();#反转列表元素　（永久改变）
message.sort();#按字母排序 顺序 列表已经改变（永久改变）
print(message);
message.sort(reverse = True)#按字母排序 逆序 列表已经改变
print(message);
print(sorted(message))#返回按字母排序的结果  列表顺序不变
print(message);
#7 遍历列表  （循环删除某个元素  remove只能删除相同元素的一个）
#通常需要确定列表长度　　len(列表)
	#值循环
for item in message:
	print(item.lower())
print(message)

numbers = ['1','2','3','2','2','2','1']
print(numbers)
while '2' in numbers:
	numbers.remove('2')
print(numbers)
print('\n')


   #数值列表循环 range(a,b)   a<=x<b  
for num in range(1,5):  
	print(num)
numbers = list(range(1,5)) #list()将数值范围转化为数值列表
print(numbers)   
                      #range(a,b,c)  a<= x <b  以c递进
numbers = list(range(2,10,2))
print(numbers)

min(numbers)
max(numbers)
sum(numbers)
#8 列表解析 创建列表
squares = [square**2 for square in range(1,11)]
print(squares)
print('***********')
nums = [num**3 for num in range(1,11)]
print(nums)
print('***********')
   #双重列表解析
N =[[randrange(10) for i in range(10)] for i in range(10)]	
print(N)
print('***********')
#9 列表的切片 [a:b] 与 range(a,b)一样    从位置a到b-1位置元素  
#切片的用法－>复制部分或者全部列表
print(squares[3:6]) #3,4,5位置
print(squares[:5])  #0，1,2,3,4位置
print(squares[-5:]);#后面5个位置

#10 复制列表  切片copys_a和变量赋值copys_b的区别
copys_a = squares[:]
copys_b = squares#squares 和 copy_b 指向的是同一个列表（类似用数组名复制）
#`其实squares　copys_b　指向的是一个列表
squares.append("different1")
copys_a.append("different2");
print(squares);
print(copys_a);

print('\n');
#其实squares　copys_b　指向的是一个列表
squares.append("num1");
copys_b.append("num2");
print(squares);
print(copys_b);

#11 检查特定值是否在列表 in  特定值不在列表中　not in
nums = list(range(1,6))
num = 6
if num in nums:
	print(str(num) + 'in nums')
else:
	print(str(num) + 'not in nums')
#列表遍历前进行判断	 列表为空 返回 false
if nums:
	for num in nums:
		print(num)
else:
	print('list is spare')
	


                                                    









