#--coding : utf-8--
#注意 字典 print() input()的书写格式 -> 字符串较长时
persons = { 
	'xiao wang' : 'shan xi',
	'xiao zheng': 'ji lin',
	'xiao chen' : 'jiang su',
	
}
xinxis = {
	'name' : 'xiao wang',
	'age'  :  25,
	'job'  : 'student',

}
#1.直接打印字典
print(persons)
print(xinxis)
print('\n')
#2.查
print('\t' + xinxis['name'].title())
print('\t' + persons['xiao wang'].title())

print('\n');
#3.改
persons['xiao chen'] = 'xia men'
xinxis['age'] = 18
print(persons['xiao chen'].title())
print(xinxis['age'])
print(persons)
print(xinxis)
print('\n');
#4.增　（１种）
persons['meng yang'] = 'song yuan'
xinxis['school'] = 'xmu'
print(persons)
print(xinxis)
print('\n')
#5.删 (１种)
del persons['xiao zheng']
print(persons)
print(xinxis['name'].title() + ' alwanys miss' +
	' in ' + persons['meng yang'].title() + ' is she ' +
	'!')
print('\n')
#6.遍历 字典没有顺序  
    #标准库collection 模块里面的 OrderedDict() 记录字典添加的键值对顺序 
   
	
	# 1.遍历 键-值对 items()返回 键-值对列表
for name , address in persons.items():
	print(name.title() + "'s home in " + address)
print('*********************')
for key , value in xinxis.items():
	print(key + ' : ' + str(value))
print('\n')
	
	# 2.遍历 键 keys() 返回键列表 -> 通过键列表可以排序 for name in sorted(persons.keys()):
print('all name is :')
for name in sorted(persons.keys()): #等价于 for name in persons 技巧：默认遍历所有键列表
	if name.title() == 'Xiao Wang':
		print(name.title() + ' always keeps ' + str(xinxis['age']));
	else:
		print('\t' + name.title());
print('*********************')	
	# 3.遍历 值 values() 返回值列表  值是可以有相同的 使用set()输出 (键是不相同的）
print('all realted message ：') #增一个相同 值
xinxis['hobby'] = 'xmu';
for values in set(xinxis.values()): #输出字典中的所有不同值 
	print('\t' + str(values));
print('\n');

#7.嵌套  ->  列表（字典）   字典（列表）  字典（字典）
	
	#7.1 列表（字典） 列表元素都是变量
xiao_wang = {
	'name':'xiao wang',
	'address':'shan xi',
	'job':'student',
}
xiao_meng = {
	'name':'xiao meng',
	'address':'sun yuan',
	'job':'computer',
}
names = [xiao_wang, xiao_meng]; #列表元素是变量 -> 一个字典
for name in names:
	print(name)
	print(sorted(name.keys()))
	print(set(name.values()))
	print('\n')
print('*********************')
for num in range(5):
	new_name = {'name':'***','adress':'***','job':'***',};
	names.append(new_name);
for name in names[:5]:
	print(name);
print('\n');
	
	#7.2字典（列表）
homes =['sun yuan','shan xi','xia men'];
humans = {
	'names': ['xiao wang','xiao meng'],
	'address' : homes,
	'language':['c','python','html'],
}
   #先遍历字典，后遍历列表
for key ,values in humans.items():
	print('\n' + key.title() + ' are :');
	if len(values)!= 0 :
		for value in values:
			if value == 'xiao wang':
				print('\t' + value + ' love she !');
			else:
				print('\t' + value);
print('\n');
    
    #7.3字典（字典）
users = {
	'xiao_wang' : xiao_wang,
	'xiao_meng' : xiao_meng,

}
for name, information in users.items():
	print(name.title() + ':')
	print('\taddress: ' + information['address'] + ' ' + str(information['job']) + 
	' misss!');
    
    
#enumerate的用法　　　针对字典返回索引以及键　与 items() 不同

#对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），
#enumerate将其组成一个索引序列，利用它可以同时获得索引和值
#enumerate多用于在for循环中得到计数

  
  
  
  
  
  
  
  

