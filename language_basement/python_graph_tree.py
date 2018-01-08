# --coding: utf-8 --
# 1.round(float_num,n) 保留N位小数 四舍五入 用于浮点数相等的比较
from random import randrange
L = [randrange(5) for i in range(100)]#列表解析 100个5以内的数
L.extend('s') #append()
#print(' '.join(L))
print(L) 
for i in range(10):
	print(i)
print("--------------------")

#2 图的表示方法 邻接表
#2.1邻接集表示    用集合           {} ->用于表示集合 散列表 字典
a,b,c,d,e = range(5)
N = [
	{b,d,e},#a
	{c,d,e},#b
	{a,d},#c
	{a,d,e},#d
	{d},#e
]
#查看某邻接点是否位于集合
if b in N[a]:
	print('true')
else:
	print('false')
print('\n')	
#2.2邻接集的字典表示
N = {
	'a' : set('bde'),
	'b' : set('cde'),
	'c' : set('ad'),
	'd' : set('ade'),
	'e' : set('d'),
}
print(N['a'])	
print('\n')
#2.3邻接列表表示  用列表
a,b,c,d,e = range(5)
N = [
	[b,d,e],#a
	[c,d,e],#b
	[a,d],#c
	[a,d,e],#d
	[d],#e
]
#输出节点C的出度
print(len(N[a]))
print('\n')
#2.4 加权邻接字典  ！！！！！！！！！重点
a,b,c,d,e = range(5)
N = [
	{b :2,d :1,e : 1},#a
	{c :2,d :3,e : 3},#b
	{a :1,d :1},#c
	{a :3,d : 4,e : 5},#d
	{d :4},#e
]
#看某边权值
print(N[a][b])
print('\n')
#2.5邻接矩阵  用0 1表示 没有权值
a,b,c,d,e, = range(5)
N = [#对角线是0
	[0,1,1,0,0],#a
	[1,0,1,1,1],#b
	[0,1,0,1,1],#c
	[0,1,1,0,1],#d
	[0,1,1,1,0],#e
	]
#存在权值 用一个无穷大的数表示边不存在
a,b,c,d,e, = range(5)
inf = float('inf')
N = [#对角线是0
	[0,3,2,inf,inf],#a
	[inf,0,inf,inf,1],#b
	[inf,inf,0,inf,1],#c
	[inf,9,5,0,8],#d
	[inf,4,2,4,0],#e
	]
#通过权值判断是否存在某条边
print(N[d][b] < inf) 

#使用列表解析创建5个节点的空列表
N = [[0]*5 for i in range(5)]

#3 树的表示    可以所使用 Bunch 模式
#3.1 用二维列表  兄弟节点写进一个列表
T = [['a','b'],['c'],['d','e']] 
#3.2 二叉树类
class Tree():
	def _init_(self,left,right):
		self.left = left
		self.right = right
#建立一个二叉树 并输出某个节点
t = Tree(Tree('a','b'),Tree('c','d'))
print(t.left.right)
#3.3 多路搜索树 -> 孩子兄弟表示法
class Tree():
	def _init_(self,kids,next = None) #将兄弟节点设为默认值 可以调节实参个数 有的没有兄弟
		self.kid = kids
		self.next = next
t = Tree(Tree('a',Tree('b',Tree('c',Tree('d'))))


























