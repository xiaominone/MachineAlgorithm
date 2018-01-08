# --coding: utf-8 --
#类 命名：驼峰法，不用下划线
#函数 模块命名：小写 下划线

class Dog( ):
    """类的格式，2个变量"""
    def __init__(self, name, age):  
		#"""定义基本属性，包括输入的实参和自定义的"""
        self.name = name  
        self.age = age
        self.size = 'big'

    def sit(self):
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        print(self.name.title() + 'is rolling')
    def update(self,newsize):
		#"""通过方法更新属性"""
        self.size = newsize
mydog = Dog('wan cai', 2)
print('mydog name is ' + mydog.name +
      '. age is ' + str(mydog.age) +
      ' .')
mydog.sit()
mydog.roll_over()
print("**********************")
#更新实例的属性值 1直接修改 2编写类方法进行修改
mydog.name = 'while'
print('mydog name is ' + mydog.name +
      '. age is ' + str(mydog.age) +
      ' .')

mydog.update('small')
print('mydog is ' + mydog.size)
mydog.sit()
mydog.roll_over()
print("***************************")

#继承  定义子类
class WhiteDog(Dog):
	"""子类的格式 supper用法 """
	def __init__(self,name,age,size = 'large'):
		super().__init__(name,age)
		self.size = size
		self.color = 'white' 
	def hobby(self):
		#子类自己的方法和属性color ,也可以重写父类的方法
		print('the dog likes ball')
		
mydog = WhiteDog('wan cai',2)
mydog.update('small')
print('mydog name is ' + mydog.name + ', age is ' + str(mydog.age)+
	", color is " + mydog.color)
mydog.sit()
mydog.hobby()
print("***************************")


class Cat():
	def __init__(self,name,age):
		"""实例当做属性"""
		self.name = name
		self.age  = age
		self.friend = WhiteDog('wang cai',3)
	def hobby(self):
		print(self.name + 'likes to play with ' + self.friend.name.title())

mycat = Cat('xiao hua',3)
mycat.hobby()
print("***************************")
		
#导入模块中的类 或者 函数

#类 命名：驼峰法，不用下划线
#函数 模块命名：小写 下划线
#OrderDict 类 创建一个字典 可以记录添加键值对顺序
from collections import OrderedDict
languages = OrderedDict()

languages['xiao wang'] = 'python'
languages['xiao meng'] = 'java'
languages['xiao pan'] = 'matlab'
languages['xiao hua'] = 'R'

for name,language in languages.items():
	print(name.title() + "'s favorite language is " +
	language.title())
		
		
		
		
