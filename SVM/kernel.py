# -*- coding: utf-8 -*-
"""
２维数据的svm　-> 属于２分类模型 

针对多类型数据　即Ａ类和不属于Ａ类　２种类别 　
本实验中为　y=０属于一类 　y!=0属于一类即y=1or2　

创建不同核函数的svm分类器　 　使用网格数据和分类器　

没有测试数据

@author: Rachel Zhang
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

iris = datasets.load_iris()
print('type of iris: ') 
print(type(iris)) #<class 'sklearn.datasets.base.Bunch'>
print('keys:')
print(iris.keys()) #['target_names', 'data', 'target', 'DESCR', 'feature_names']

X = iris.data[:,:2] #only use the first two features
Y = iris.target
#print(np.shape(X)) 训练数据集前２列　 150*2 方便画图 
#print(np.shape(Y))　训练数据集标签Ｙ　150*1 
#print(Y) Y有３类0 1 2

# create instances of svm  创建不同核函数的svm　的分类器 分类器对象clf
linear_svc = svm.SVC(kernel = 'linear').fit(X,Y)#W'x
rbf_svc = svm.SVC(kernel = 'rbf', gamma = 0.7).fit(X,Y)
poly_svc = svm.SVC(kernel = 'poly', degree = 3).fit(X,Y)


# create a mesh 绘制网格　（利用已经创建的分类器和网格数据，画出对应的分割平面）
x0_min, x0_max = X[:,0].min()-0.1, X[:,0].max()+0.1
x1_min, x1_max = X[:,1].min()-0.1, X[:,1].max()+0.1
h = .02 # step size in the mesh
#meshgrid(array1,array2) 组合数据　生成２个２维度的数组　
# 第一个二维数组　array1 的行向量　重复　len(array2)行
# 第二个二位数组　array2 的行向量转为列向量　重复len(array1)列
xx,yy = np.meshgrid(np.arange(x0_min,x0_max,h),np.arange(x1_min,x1_max,h))


#print(np.shape(xx))
#print(np.shape(yy))
#print()
titles = ['linear','rbf','poly']
for i,clf in enumerate((linear_svc,rbf_svc,poly_svc)):
	plt.subplot(1,3,i+1)
	plt.subplots_adjust(wspace = 0.4, hspace = 0.4)
	#np_c 以列向量进行组合　np.r_ 以行向量进行组合
	#压缩数据到一维　xx.ravel()
	#print(xx.ravel().shape)
	#网格数据的分类Z 分类器对象clf 预测网格数据的标签
	Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
	#Z = clf.decision_function(np.c_[xx.ravel(),yy.ravel()])
	
	#print((np.c_[xx.ravel(),yy.ravel()]).shape)
	#print(Z.shape)
	#print(xx.shape)
	Z = Z.reshape(xx.shape)
	#print(Z)
	#Z = np.random.randint(0,3,xx.shape)  
	
	#draw decision boundary
	#根据网格数据的预测标签划分区域　　不同颜色的区域对应相应的类别
	plt.contourf(xx,yy,Z,cmap = plt.cm.cool)
	#训练数据在分类器上的展示  
	plt.scatter(X[:,0],X[:,1],c = Y,cmap = plt.cm.cool)
	plt.title(titles[i])
plt.show()
