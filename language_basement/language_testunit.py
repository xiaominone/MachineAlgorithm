# --coding: utf-8 --
#学习测试模块 unittest  测试用例是一组单元测试     
#               timeit 会多次计算得出平均运行时间
#                cprofiler 测试某函数运行时间 
#                 trace 每条语句执行次数
#                 Python Call Graph 可视化代码调用情况
from 待测试模块module_name  import 待测试函数 Function_name
import unittest
class FunctionNameTest(unittest.TestCase):#父类 TestCase 使用相关的断言函数
	def setUp(self):#若有setUp(self) 要先于test_开头的函数执行 用于生成每个单元测试中的公共内容
	def test_functionname1(self):#以test_开头的函数 自动执行 第一个单元测试
	def test_functionname2(self):#第二个单元测试
	.........	
#setUp()解析
测试自己的类时，该方法让测试单元函数变得简单，可在setUp()方法中建立一系列实例并设置属性，
在测试单元函数中直接使用这些实例，比在实例中建立实例，设置属性  简单很多




#继承到的断言函数：
self.assertEqual(a,b)
self.assertNotEqual(a,b)
self.assertTrue(X)
self.assertFalse(X)
self.assertIn(item,list) 核实item在列表中		


#运行
unittest.main()

#运行结果分析：
....  代表4个测试单元通过
E 有一个测试单元出错 后面跟相应的traceback
末尾 OK 或者 FAILED
