#谱聚类方法
#k1 近邻图　用于求权值矩阵w
#k2 用于选择的前k2特征向量
#k3 k3-mean的k3确认　　也可以使用密度聚类的方法 

#求　正则化的随机游走　拉普拉斯矩阵
def laplace_matrix(data,neighbor):
#m个样本　  初始化相似度图的权值矩阵 w
	m = len(data)
	w =[[] for x in range(m)]
	for i in range(m):
		w[i] = [0 for x in range(m)]
	# 等价于　w = np.zeoros((m,m)) 
		
	#使用k-近邻图求权值矩阵w　　　自定义neighbor　
	#每个样本都要求一个nearest列表 定义为距离列表　　
	nearest = [-１ for x in range(neighbor)]
	
	for i in range(m):
		#初始化每个样本的k-近邻列表
		zero_list(nearest)
		nearest = clc_nearest(data,i,neighbor) #求第i个数据的k近邻的 距离列表 可以使用堆排序
		for j in range(i+1,m):
			w[i][j] = similiar(data,i,j)#计算第i个样本和第j个样本的相似度（常用高斯相适度）
			if　not is_neighbor(w[i][j],nearest): 
			#判断j是不是i的邻居　不是的话权值为０ 　需要使用近似距离相等　w[i][j]距离不可能完全相等于nearest里面的值
				w[i][j] = 0
			w[i][j] = w[j][j] #对称矩阵　
		w[i][i] = 0 #对角线上的元素是０
	
	#根据权值矩阵求随机游走拉氏矩阵　　
	for i in range(m):
		s = 0
		for j in range(m):
			s += w[i][j]
		if  s==0
			pirnt('矩阵第 ' + str(i) + ' 行全为０')
			continue
		for j in range(m):
			w[i][j] /= s
			w[i][j] = -w[i][j]
		w[i][j] += 1
		
	return w
	
#返回样本x[i]最近的neighbor邻居 使用最小堆排序　　输出前neighbor个最近的邻居样本
def	 clc_nearest(data,i,neighbor)
	m = len(data)
	nearest_distance = [-１ for x in range(m-1)]
	for j in range(m):
		if j!=i :
			nearest_distance [j] = similiar(data,i,j)
		
			
	#使用堆排序输出最近的neighbor样本距离列表　
	nearest_distance = heapq.nsmallest(neighbor, nearest_distance)
	
	return nearest_distance 
		
def similiar()
#计算样本之间的高斯相似度
	return
	
def spectral_cluster(data)
#普聚类　　对拉氏矩阵求特征向量组成的样本　然后对其使用k_mean
	lm = laplace_matrix(data,neighbor)
	eg_values,eg_vectors = np.ling.eig(lm)
	idx = np.argsort(eg_values)#获得从小到大特征值排序的索引
	eg_vectors = egvectors[:,idx]#特征向量以列向量给出　按照特征值大小排序
	
	m = len(data)
	eg_data = [[] for x in range(m)] #计算k个特征向量组成的矩阵　m行k列 表示m个样本
	for i in range(m):
		eg_data[i]=[0 for x in range(k)]
		for j in range(k):
			eg_data[i][j] = eg_vectors[i][j]
	return k_mean(eg_data)
	
		
		
		
		
		
		
		
		
		
