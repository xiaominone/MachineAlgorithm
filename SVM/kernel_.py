"""
2分类svm y = 1 or y = 2 

有训练数据和测试数据集
2种画图方式
1. 计算网格点到超平面的距离(clf.decision_function) 并建立等高线
２. 对网格数据进行预测(clf.predict) 建立着色图，不同颜色的区域就是分类器定义的相应类别的区域

"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data#数据Ｘ
y = iris.target#类别Y

#仅使用２类数据
X = X[y != 0, :2]#取类别不等于０的数据的前２维
y = y[y != 0]#与数据相应的标签　y = 1 or y =2

#使用所有类别数据　但将　y=0视为一类　y!=0视为一类
#X = X[:,:2]#取类别不等于０的数据的前２维
#y = y[:]#与数据相应的标签　y = 0 or y =1 or y=2

n_sample = len(X) #样本的数量
print(n_sample)
np.random.seed(0)
order = np.random.permutation(n_sample)#返回n_sample个伪随机数，返回值是一个array
X = X[order]#打乱数据集
y = y[order].astype(np.float)

X_train = X[0:int(0.9 * n_sample)]#训练数据集 前　90％
y_train = y[:int(0.9 * n_sample)]
X_test = X[int(0.9 * n_sample):]#测试数据集 后　10％ 
y_test = y[int(0.9 * n_sample):]
#print(X_test.shape)
#print(y_test.shape)
# fit the model
for fig_num, kernel in enumerate(('linear', 'rbf', 'poly')):
	#选择核函数　构建分类器对象clf　
	clf = svm.SVC(kernel=kernel, gamma=10)
	#填充训练数据　建立分类器
	clf.fit(X_train, y_train)
	
	#fig_num    0-2
	plt.figure(fig_num)
	#画出分类器
	plt.clf()
	#显示训练数据集的　离散点　２分类问题　根据颜色映射显示类别
	plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, zorder=10, cmap=plt.cm.cool)

    # 显示测试数据 －> 点大的是测试数据 颜色深浅显示标签
	plt.scatter(X_test[:, 0], X_test[:, 1],c=y_test,cmap=plt.cm.cool,s=100, facecolors='none', zorder=10)
	
	#构建网格数据　绘制等高线
	plt.axis('tight')
	x_min = X[:, 0].min()
	x_max = X[:, 0].max()
	y_min = X[:, 1].min()
	y_max = X[:, 1].max()
	#产生２个矩阵XX YY  然后压缩ravel到一维
	XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
	#计算网格点到超平面的距离　decision_function
	Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
	#使用分类器的　对网格数据预测数据
	#Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
	Z = Z.reshape(XX.shape)
	
	
	#绘制３条等高线的　分别是　-0.5  0  0.5　距离超平面的距离　decision_function
	C = plt.contour(XX, YY, Z,colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
		levels=[-.5, 0, .5])
	plt.clabel(C, inline = True, fontsize = 10)
	
	#plt.contourf(XX,YY,Z,cmap = plt.cm.cool)
	

	plt.title(kernel)
plt.show()











