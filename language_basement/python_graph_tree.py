# --coding: utf-8 --
# 1.round(float_num,n) ����NλС�� �������� ���ڸ�������ȵıȽ�
from random import randrange
L = [randrange(5) for i in range(100)]#�б���� 100��5���ڵ���
L.extend('s') #append()
#print(' '.join(L))
print(L) 
for i in range(10):
	print(i)
print("--------------------")

#2 ͼ�ı�ʾ���� �ڽӱ�
#2.1�ڽӼ���ʾ    �ü���           {} ->���ڱ�ʾ���� ɢ�б� �ֵ�
a,b,c,d,e = range(5)
N = [
	{b,d,e},#a
	{c,d,e},#b
	{a,d},#c
	{a,d,e},#d
	{d},#e
]
#�鿴ĳ�ڽӵ��Ƿ�λ�ڼ���
if b in N[a]:
	print('true')
else:
	print('false')
print('\n')	
#2.2�ڽӼ����ֵ��ʾ
N = {
	'a' : set('bde'),
	'b' : set('cde'),
	'c' : set('ad'),
	'd' : set('ade'),
	'e' : set('d'),
}
print(N['a'])	
print('\n')
#2.3�ڽ��б��ʾ  ���б�
a,b,c,d,e = range(5)
N = [
	[b,d,e],#a
	[c,d,e],#b
	[a,d],#c
	[a,d,e],#d
	[d],#e
]
#����ڵ�C�ĳ���
print(len(N[a]))
print('\n')
#2.4 ��Ȩ�ڽ��ֵ�  �������������������ص�
a,b,c,d,e = range(5)
N = [
	{b :2,d :1,e : 1},#a
	{c :2,d :3,e : 3},#b
	{a :1,d :1},#c
	{a :3,d : 4,e : 5},#d
	{d :4},#e
]
#��ĳ��Ȩֵ
print(N[a][b])
print('\n')
#2.5�ڽӾ���  ��0 1��ʾ û��Ȩֵ
a,b,c,d,e, = range(5)
N = [#�Խ�����0
	[0,1,1,0,0],#a
	[1,0,1,1,1],#b
	[0,1,0,1,1],#c
	[0,1,1,0,1],#d
	[0,1,1,1,0],#e
	]
#����Ȩֵ ��һ������������ʾ�߲�����
a,b,c,d,e, = range(5)
inf = float('inf')
N = [#�Խ�����0
	[0,3,2,inf,inf],#a
	[inf,0,inf,inf,1],#b
	[inf,inf,0,inf,1],#c
	[inf,9,5,0,8],#d
	[inf,4,2,4,0],#e
	]
#ͨ��Ȩֵ�ж��Ƿ����ĳ����
print(N[d][b] < inf) 

#ʹ���б��������5���ڵ�Ŀ��б�
N = [[0]*5 for i in range(5)]

#3 ���ı�ʾ    ������ʹ�� Bunch ģʽ
#3.1 �ö�ά�б�  �ֵܽڵ�д��һ���б�
T = [['a','b'],['c'],['d','e']] 
#3.2 ��������
class Tree():
	def _init_(self,left,right):
		self.left = left
		self.right = right
#����һ�������� �����ĳ���ڵ�
t = Tree(Tree('a','b'),Tree('c','d'))
print(t.left.right)
#3.3 ��·������ -> �����ֵܱ�ʾ��
class Tree():
	def _init_(self,kids,next = None) #���ֵܽڵ���ΪĬ��ֵ ���Ե���ʵ�θ��� �е�û���ֵ�
		self.kid = kids
		self.next = next
t = Tree(Tree('a',Tree('b',Tree('c',Tree('d'))))


























