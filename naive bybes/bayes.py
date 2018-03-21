'''
Created on 2016.11

@author: Peter
'''
from numpy import *
#载入一些实验数据  已经切割好的词向量 
#postingList 定以了切割后的6个文本向量
#classVec 6个文本的类别（2分类）
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
    
#创建一个包含文档所有出现的单词的 不重复列表  返回词汇表vocabSet               
def createVocabList(dataSet):
	#列表的空集合
    vocabSet = set([])  #create empty set
    for document in dataSet:
		#操作符 |   求2个集合的并集
        vocabSet = vocabSet | set(document) 
    #将集合再转化为列表    
    return list(vocabSet)

#setOfWords2Vec（）函数使用词汇表vocabSet以及一个训练文档 
#返回训练文档的文档向量  
#文档向量中的0 1 表示文档是否出现词汇表中词   没有考虑词频 --》词集模型
#长度与词汇表vocabSet一致
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    #循环检测文档中的所有单词
    for word in inputSet:
		#如果单词在词汇表中出现 向量为1 没有考虑词频
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: 
			
			print "the word: %s is not in my Vocabulary!" % word
    return returnVec
#文档向量考虑出现词汇表中单词的个数  --》词袋模型    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

#朴素贝叶斯的训练函数  2分类
#首先需要构造词汇表 将每个训练样本调用setOfWords2Vec（）得到每个文档向量 组成trainMatrix 
#训练样本（列表的列表） 是对应的文档向量   trainMatrix  
#训练样本的类别（列表） trainCategory
def trainNB0(trainMatrix,trainCategory):
	#numTrainDocs 训练样本的个数
    numTrainDocs = len(trainMatrix)
    #numWords  每个样本的长度即文档向量的长度
    numWords = len(trainMatrix[0])
    #二分类
    #样本类别是 0 or 1  pAbusive 是类别1的先验概率
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    #应用到拉普拉斯平滑处理 防止出现条件概率为0
    #p0Num  单位行向量
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    for i in range(numTrainDocs):
		#判断训练样本属于哪一个类别
        if trainCategory[i] == 1:
			#分子p1Num 是向量相加      基向量 p1Num 与训练文档向量 trainMatrix[i]
            p1Num += trainMatrix[i]
            #分母p1Denom 是一个数 类别1的样本中出现词汇表中的词的总个数
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
	#类别1下的条件概率 p1Vect
	#类别0下的不同特征的条件概率求和  p0Vect
	#取对数避免下溢
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive

#计算测试样本vec2Classify分类结果结果
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
	#避免下溢 求和 
	#属于哪种类别的概率大即为哪种类别
	#vec2Classify 测试样本的向量 由 0或1 组成
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    

#完整的一个朴素贝叶斯模型案例
def testingNB():
	#载入训练数据
    listOPosts,listClasses = loadDataSet()
    #创建词汇表
    myVocabList = createVocabList(listOPosts)
    #创建并初始化训练文档的矩阵trainMat 使用词集模型
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
        
    #使用numpy数组 用array转化 返回条件概率 先验概率   
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    #使用测试文档 并转化为文档向量thisDoc
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)

#模拟实例 垃圾邮件分类
#准备数据  切割文本 使用模块re
#input is big string, #output is word list
def textParse(bigString):   
	#正则表达式进行切割 
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] 

#主程序 
#1 训练样本 组成词汇表 vocabList
#2 构造训练样本 trainingSet 
#3 调用分类函数 trainNB0（）
#4 统计准确率
def spamTest():
	#定以词汇表 docList 列表的列表
    docList=[];
    #类别表 
    classList = []; 
    #将所有文本切割后的列表 fullText 包含每个文本的单词
    fullText =[]
    #利用训练数据
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        #append（）的用法 加列表wordList加到列表docList尾部
        docList.append(wordList)
        #extend（）的用法 将列表wordList的元素加到列表fulltText尾部
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
	#利用docList建立词汇表 每一个样本是一个列表
    vocabList = createVocabList(docList)#create vocabulary
    #随机构造一个训练集trainingSet
    trainingSet = range(50); 
    #选择的训练样本的索引列表
    testSet=[]  
    #利用产生的索引建立训练集
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; 
    trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)
    #return vocabList,fullText
 
 
 
 
    
#使用贝叶斯分类器从广告中获取区域倾向

#RSS源分类器及高频词去除函数
#词汇表 vocabList
#每个训练文本的所有单词和 的列表（有重复单词）  fullText
def calcMostFreq(vocabList,fullText):
    import operator
    #字典用 freqDict 来统计词汇表中出现的频数 （使用所有单词的列表 fullText）
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    #对字典的值进行排序 返回频率前30的词汇
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True) 
    return sortedFreq[:30]       

#从个人广告中获取区域倾向
#主程序 
#使用2个RSS源内容 作为参数输入 feed1 feed0
#feed1=feedparser.parse("http://........")
def localWords(feed1,feed0):
	#模块 feedparser 用于R获得RSS源内容
    import feedparser
    #docList 每个文档的词汇表组成的列表
    #fullText 所有文档的所有单词组成的列表
    docList=[]; 
    classList = [];
    fullText =[];
    # feed1['entries'] 获得feed1源的所有条目的列表
    # 找到2个源中 条目长度的最小值 minLen
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
		#feed1['entries'][i]['summary']获得条目列表中第i个条目的sumaary部分
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) #NY is class 1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
	#建立词汇表 并将频率最高的前30个元素移除
    vocabList = createVocabList(docList)#create vocabulary
    #top30Words是前30个词汇   remove top 30 words
    top30Words = calcMostFreq(vocabList,fullText)  
    # top30Words 以列表的列表存在
    for pairW in top30Words:
        if pairW[0] in vocabList: 
			vocabList.remove(pairW[0])
    trainingSet = range(2*minLen); testSet=[]  
    
    
    #建立训练数据 trainingSet
    #建立训练数据矩阵 trainMat
    
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    #对每一个训练数据进行分类
    for docIndex in testSet:       
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V

#最具表征性的词汇显示函数 返回大于某个阈值的所有词汇 
#ny sf是获得的RSS源内容 ny=feedparser.parse("http://........")
def getTopWords(ny,sf):
    import operator
    #p0v p1v是训练数据的先验概率 和 条件概率
    vocabList,p0V,p1V=localWords(ny,sf)
    #获得2个源的条件概率大于-6.0 的词汇元组
    topNY=[]; topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    #sortedSF是元组
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]
