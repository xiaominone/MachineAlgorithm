#采用ID3构造决策树
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

#计算数据集的熵
def calcShannonEnt(dataSet):
	#numEntries 训练样本的数量
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        #获得样本的标签 并添加到字典中 计算不同标签的样本数量
        currentLabel = featVec[-1]
        #等价于下面3行代码 labelCounts[currentLabel] = labelCounts.get(currentLabel,0)+1
        if currentLabel not in labelCounts.keys(): 
			labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    #初始化数据集 熵的值
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        #熵的计算公式
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt
    
#按照给定的特征以及特征值划分数据集, 返回 按照对应特征以及特征值 划分后的样本，并切除了该特征
#    dataSet待划分数据集  axis划分特征  value划分特征的特征值
def splitDataSet(dataSet, axis, value):
	#方便划分 每次划分都建立一个列表对象 好处：不用在同一个列表上操作
    retDataSet = []
    for featVec in dataSet:
		#划分数据集的特征axis ,统计某个样本axis特征等于values 将这个样本的axis特征切片处理
		#为什么切掉axis特征  为了方便下一次划分 不在使用这个特征 #chop out axis used for splitting
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            #extend()和append()的区别   
            #extend（）将添加的元素添加到列表  
            #append（）将添加的数据结构置于列表尾部   
            reducedFeatVec.extend(featVec[axis+1:]) 
            retDataSet.append(reducedFeatVec)
    return retDataSet#列表的列表 将样本中特征axis等于value的进行切片 并组合成新的列表

#如何选择最后的划分方式  使用信息增益 返回最优特征   
def chooseBestFeatureToSplit(dataSet):
	#所有特征numFeatures数量   有一个是标签需要减一
    numFeatures = len(dataSet[0]) - 1   
    #求原始数据集的熵
    baseEntropy = calcShannonEnt(dataSet)
    #定以信息增益 最优特征
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #从所有特征中选择最优特征
		#创建一个列表，保存每个样本对应特征的所有特征值 
		#特征值列表 
        featList = [example[i] for example in dataSet]
        #使用集合 获得特征值列表中不同元素的列表
        uniqueVals = set(featList)  
        #按特征划分后的样本的熵     
        newEntropy = 0.0
        #for用来计算特征i下不同特征值的熵的和
        for value in uniqueVals:
			#使用第i个特征中某一个特征值value划分
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            #累加不同value下的熵 即为条件熵 
            newEntropy += prob * calcShannonEnt(subDataSet)  
        #特征i下的信息增益       
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

#在所有特征都使用后，还不能划分数据集，采用多数表决确定类别（看哪一类）
def majorityCnt(classList):
	#定以一个字典 确定不同类别的数量
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): 
			classCount[vote] = 0
        classCount[vote] += 1
    #对字典排序  sorted（） 返回列表的列表 
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    #返回字典中类别数量最多的类别
    return sortedClassCount[0][0]

#递归构造决策树 递归结束条件 ：1.所有特征使用完 2.每个分支下所有实例具有相同特征
#label 特征向量（包括类标签）
def createTree(dataSet,labels):
	#classList 所有训练样本的类标签列表
    classList = [example[-1] for example in dataSet]
    #stop splitting when all of the classes are equal 所有的类是 一样的
    if classList.count(classList[0]) == len(classList): 
        return classList[0]
    #stop splitting when there are no more features in dataSet 所有特征都被划分完
    if len(dataSet[0]) == 1: 
		#使用多数表决决定返回的类标签
        return majorityCnt(classList)
    #对dataSet进行划分 返回最优特征的索引    
    bestFeat = chooseBestFeatureToSplit(dataSet)
    #得到特征bestFeatLabel 并以此为根节点
    bestFeatLabel = labels[bestFeat]
    #建立决策树myTree
    myTree = {bestFeatLabel:{}} #字典的字典
    #删除此特征
    del(labels[bestFeat])
    #每个样本bestFeat特征的特征值的列表featValues  并求集合
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
		#subLabels是删除过最优标签的列表
        subLabels = labels[:]   
        #copy all of labels, so trees don't mess up existing labels
        #使用最优特征进行划分的样本 和 删除过最优特征的标签subLabels 进行递归建树
        #myTree树  字典的字典  节点是特征
        #特征是节点 每个特征值是权值 特征值个数对应分支数 
        #createTree(splitDataSet(dataSet, bestFeat, value),subLabels) 返回类别或者子树
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
        #{'特征a':{0：类别，1：{子树}}}  0 or 1 是特征a 的取值  
    return myTree                            


#测试算法    使用决策树的分类函数
#inputTree 决策树 
#featLabels 所有的特征列表
#testVec 测试样本的特征 对应的向量
def classify(inputTree,featLabels,testVec):
	#决策树的第一个最优特征firstStr
    firstStr = inputTree.keys()[0]
    #最优特征下的字典secondDict
    secondDict = inputTree[firstStr]
    #最优特征在所有特征中的索引featIndex
    featIndex = featLabels.index(firstStr)
    #测试样本对应最优特征的特征值key
    key = testVec[featIndex]
    #查看样本最优特征下的特征值 对应的是类别 还是字典
    valueOfFeat = secondDict[key]
    #判断返回的是字典还是类别
    if isinstance(valueOfFeat, dict): 
		#字典 继续递归
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    #返回测试样本的类别
    return classLabel

#使用pickle模块 存储决策树  构建决策树花费大量时间 所有需要保留 避免重复构建
def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
    
