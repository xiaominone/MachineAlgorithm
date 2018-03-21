'''
Created on  2016 10.11
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

'''
from numpy import *
import operator
from os import listdir

# 用于分类的输入向量inX 输入的样本样本集dataset 标签向量labels 最近邻居数目Ｋ
def classify0(inX, dataSet, labels, k):
	#dataSetSize样本数目（数据集矩阵的行数）    shape[0]矩阵行数
    dataSetSize = dataSet.shape[0]
    #diffMat    扩展输入向量inX （与dataSet相同规模矩阵）
    #  tile（A,（m，n））  将矩阵A 的横 纵做相应扩展
    # 与数据集dataSet矩阵相减   测试样本与所有样本的各维度差矩阵
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    #使用欧氏距离  距离差的平方 （矩阵个元素的2次方）
    sqDiffMat = diffMat**2
    #将差的平方矩阵的行向量求和 //行向量求和sum（axis=1）  开根号就是相应的欧氏距离
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    #argsort()函数返回矩阵从小到大的索引值  返回值也是 矩阵 sortedDistIndicies
    sortedDistIndicies = distances.argsort()
    #建立类的字典  类别是键  个数是值
    classCount={}          
    for i in range(k):
        #找到前k个距离最近样本 通过索引矩阵sortDistIndicies  将类别作为键进行初始化字典
        voteIlabel = labels[sortedDistIndicies[i]]
        #dict.get(key, default=None) 返回键key的值 若键不存在，返回default默认值
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #  将字典按 值 倒序排序 python2.x 中iteritems（）返回迭代器对象列表  python3.不再用
    # sort()返回 列表 （二维） ortedClassCount[0][0]是频数最大的标签
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

#导入数据集
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    # groupe 数组 label 列表
    return group, labels

# 从文本文件中解析数据 转化为numpy可以解析的
def file2matrix(filename):
    fr = open(filename)
    #文本文件的行数numberOfLines
    numberOfLines = len(fr.readlines())
    # 样本的初始矩阵 numberOfLines*3 的零矩阵
    returnMat = zeros((numberOfLines,3))
    # 样本标签向量
    classLabelVector = []

    index = 0
    for line in fr.readlines():
        #删除每行的左右空格 （行俩端的空格，内部删除不了）
        line = line.strip()
        #以制表符进行切割 split('\t') 返回的是列表
        listFromLine = line.split('\t')
        #矩阵returnMat的index行被重新赋值
        returnMat[index,:] = listFromLine[0:3]
        #标签向量对应样本 列表listFromLine[-1]  最后一个元素
        classLabelVector.append(int(listFromLine[-1]))
        #更改index 修改样本矩阵的每一行
        index += 1
    return returnMat,classLabelVector
#归一化特征值 将特征值转化为0-1之间
# newvalues=(oldValues-min)/(max-min)  转化为相同规模的矩阵操作
def autoNorm(dataSet):
    #dataSet是numpy矩阵     min（0）表示在矩阵列中找最小值 返回一个行向量，是各列的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    #ranges 每列数据最大值与最小值的差 的 行向量（3列）
    ranges = maxVals - minVals
    #创建相同规模的矩阵    shape（matrix）返回矩阵的行列数
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    #矩阵对应值的除法  Numpy库中linalg.solve(matA,matB)表示矩阵除法
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

#测试数据 得出测试的错误率
def datingClassTest():
    # hoRatio用于确定测试样本占总样本的百分比
    hoRatio = 0.50
    #文本解析出数据 然后对数据归一化处理
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    #获得测试样本的数量numTestVecs
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        #第i个测试样本进行KNN处理 注意数据的切分 哪些用于已知 哪些测试
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ("the classifier came back with: "+ str(classifierResult) +
               "the real answer is: " +  str(datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print ("the total error rate is: "+str (errorCount/float(numTestVecs)))
    print (errorCount)

 #将32*32 的二进制图像矩阵转化为1*1024的向量
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
#手写体识别测试代码
def handwritingClassTest():
    #样本的标签向量
    hwLabels = []
    #listdir （）返回给定文件下的文件名称列表
    trainingFileList = listdir('trainingDigits')
    #m个文件（样本）
    m = len(trainingFileList)
    #获得数据的初始零矩阵 trainMat
    trainingMat = zeros((m,1024))
    for i in range(m):
        #对第i个样本操作 获得文件名称fileNameStr
        fileNameStr = trainingFileList[i]
        #对文件名称进行操作  例如 0_1.txt
        fileStr = fileNameStr.split('.')[0]
        #classNumStr 样本的标签  例如 0_1.txt是0
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        #样本的矩阵
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        #对测试样本采用相同的操作
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        #测试数据i 的真实标签classNumStr
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        #进行样本测试
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))
