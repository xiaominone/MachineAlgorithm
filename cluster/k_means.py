#--coding: utf-8 
#随机选择簇中心的k-mens算法
def k_means(data,k=5) #默认实参为５类
#m个样本　维度为n
	m = len(data)
	n = len(data[0])
	
	#m个样本的样本的对应的簇中心cluster 　　存放的是cluster_center的索引
	cluster = [-1 for x in range(m)]
	cluster_center = [[] for x in range(k)]
	
	#用于求下一轮的k个聚类中心位置　　即上一轮属于某个簇的所有数据的均值
	#cc = [[] for i in range(k)]
	cc = [ np.zeros(n) for i in range(k)] #用于求下一轮的k个簇中心
	
	#c_number  每个簇中的样本数量　和cc一起用于求下一轮的簇中心位置
	c_number = [0 for x in range(k)]
	
	##随机选择k个聚类中心
	i = 0
	while i < k:
		#在样本中随机选择一个样本作为簇中心　（也不一定要是样本中的值）
		j = random.randint(0,m-1)
		#判断该样本是否已经入选中心列表　 或者　与入选的样本中心有相似的
		if data[j] in cluster_center:　　#is_similar(data[j],clustr_center):
			continue
		cluster_center[i] = data[j][:]
		
		#cc[i] = [0 for x in range(n)]#用于求下一轮第i个粗簇中心 　　cc完成初始化
		i += 1
		
	for times in range(40):
		#定义４0的迭代次数
		#对m个样本进行分类　　（按照欧式距离）
		for i in range(m):
			#返回i样本最近的那个簇中心的索引c
			c = nearest(data[i],cluster_center)
			cluster[i] = c　#每个样本对应的簇中心
			
			#第c个簇中心的样本数量加１
			c_number[c] += 1 
			
			#将样本data[i]加入到cc[c]　用于下一轮的簇中心 
			add(cc[c],data[i])
			
		for i in range(k)
			#更新第i个簇的中心
			divide(cc[i],c_number[i])
			cluster_center[i] = cc[i][:]
			
			#从新开始计算第i个簇中心的样本数量
			c_number[i] = 0
			
			#从新开始计算第i个簇中心的样本累加和　
			zero_list(cc[i])
		print(times)
		print(cluster_center)
		
 return cluser
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
