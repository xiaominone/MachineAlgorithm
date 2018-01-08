#coding: utf-8 
#常使用：　１．默认形参（放在形参列表最后，可显示修改）、　位置实参　关键字实参、
		#　2.利用默认形参为空　使实参变为可选
		#3 接受任意数量的实参 * 　**（放在形参列表表尾　默认封装为元组）

def print_greet(user_name):
	"""函数说明生成文档"""
	print('hello ' + user_name.title())
print_greet('xiao wang')

def print_greet(user_name):
	""" 打招呼 """
	greet = 'hello ' + user_name;
	return greet;
name = print_greet('xiao wang')
print(name)
print('**********************')
    

def describe_pet1(animal_type,pet_name):
	"""位置实参调用"""
	print('i have a '+ animal_type);
	print('name is ' + pet_name);
describe_pet1('dog','huahua')
print('\n')

def describe_pet2(animal_type,pet_name):
	"""关键字实参调用"""
	print('i have a '+ animal_type);
	print('name is ' + pet_name);
describe_pet2(animal_type='dog',pet_name='huahua')
print('\n')
print('**********************')

def describe_pet(pet_name,animal_type='dog'):
	"""形参定义为默认值，仍可以修改。当大部分参数有默认值时使用，且放在最后，不要将位置实参与关键字实参混淆"""
	print('i have a '+ animal_type);
	print('name is ' + pet_name);
describe_pet('huahua')
describe_pet('huahua','cat')
describe_pet(pet_name='huahua',animal_type='cat')
print('\n')
print('**********************')

def get_fullname(first,last,middle=''):
	"""当形参定义为空，实参可选可不选,默认值的特殊情况"""
	if middle:
		fullname = first + middle + last
	else:
		fullname = first + last
	print(fullname)
get_fullname('M','y')
get_fullname('wang','min''min')		

def greetusers(names):
	""" 形参为列表  """
	for name in names:
		mes = 'hello,' + name
		print(mes)
usernames = ['xiaowang','xiaozhao']
greetusers(usernames)

def trans_address(stayed,address):
	"""复制列表，也可以使用切片"""
	while stayed:
		stay = stayed.pop();
		address.append(stay);
	print(address)

def show_address(adress):
	"""遍历列表"""
	for adres in adress:
		print('\t' + adres.title());	
adress = []
stayed = ['cahng zhi','chang chun','bei jing','shang hai','xia men','xia men','xia men','xia men'];
trans_address(stayed,adress);
show_address(adress);
print('**********************')
 
def get_fullname(firstname,secondname,age=''):
	"""返回一个字典 """
	"""形参为默认值，可选可不选"""
	person = {'first':firstname,'second':secondname};
	if age:
		person['age'] = age;
	return person;
people = get_fullname('xiao ','wang')
print(people)
people = get_fullname('xiao','meng',age=24)
print(people)
print('**********************')
 
#禁止函数修改列表 使用切片创建副本作为实参



########################################
#实参前面加*  表示创建一个对应的元组，可以接受多个实参
#首先匹配位置实参和关键字实参，最后将剩下的实参放到一个元组 
def tvshow(p,q='',*names):
	"""位置实参p 默认可选q 接受任意数量实参的names元组"""
	if q:
		print(p +' ' + q +' both like:');
	else:
		print(p + ' likes some TV:');
	for name in names:
		print(name);
tvshow('xiao wang','xiao meng','cctv','pptv','mtv')
print('\n');

#** 添加任意数量的键值对形参　（实参的键不需要引号）
def user_infor(p,**users):
	"""接受任意数量的键值对"""
	print(p + ' is ?')
	profile = {}
	for key,value in users.items():
		profile[key] = value
		print(key + ' : ' + value)
user_infor(p='haha',name='xiaowang',loacation='xia men',job='student')

