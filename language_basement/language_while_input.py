#学习while   以及交互式操作 input()
#while　用于列表的修改　　列表之间的移动
#for　列表之间的遍历 
   #input()将内容打印到屏幕，作为提示内容 并且接受用户输入作为变量内容
message = input('hello, wellcome here , yes or no ?');
print('\t your answer is '+ message);
   #当输入提示内容较多时，使用 += 将提示内容定义一个变量
message_1 = 'if you want to be who ?, please you can'
message_1 += '\nkeep to think ,and your answer is yes or no ? '

while True:
	answer = input(message_1);
	if answer == 'yes':
		print('\tyour answer is ' + answer);
	else:
		break;

#while 用于修改列表 字典	 for更多用于遍历，不用于修改
  
  #列表之间移动元素
adress = [];
stayed = ['bei jing','shang hai','xia men','xia men','xia men','xia men']
print(stayed)
while stayed:
	stay = stayed.pop()
	adress.append(stay)
print(adress)

  
  #删除列表元素 remove() 删除第一个指定元素 不能删除全部特定元素 也可以使用set转换
while 'xia men' in adress:
	adress.remove('xia men')
print(adress);
  
  #用于用户不断添加元素到列表、字典
sense = {}
flag = True
while  flag:
	#存储信息
	name = input('your name: ')
	sense1 = input('love is what? ')
	#添加到字典
	sense[name] = sense1
	#判断是否结束
	message_1 = 'do you wang to continue , '
	message_1 += 'input your answer（yes/no） ? '

	ans = input(message_1.title());
	if ans == 'no':
		flag = False;
	else:
		continue;
print(sense)
