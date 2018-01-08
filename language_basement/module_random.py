#Python中的numpy.random模块  用于生成随机数 
#random.方法　　或者　　np.random.方法　　　（注意使用方法）



#0 np.random.rand()  产生均匀分布的样本值 0-1范围内 只能是一维数组 可以扩大到相应范围
 eg ：np.random.rand(4) 产生4个0-1范围内的值
#  binomial 产生二项分布的样本值  beta  Beta分布的样本值   gamma  伽马分布样本值

#1 np.random.random
np.random.random(4)  #产生4个0-1范围内的值
np.random.random(size=(2,2))#0 <= n < 1.0 2*2列随机矩阵
np.random.rand(2,2) #0 <= n < 1.0 2*2列随机矩阵
#2 np.random.uniform　或者　random.uniform
random.uniform的函数原型为：random.uniform(a, b)
用于生成一个指定范围内的随机符点数，
两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b 如果 a <b， 则 b <= n <= a
1 参数为空默认生成一个[0,1)均匀分布的值 
2 参数为1个的时候  uniform(a)   生成一个[0,a)均匀分布的值

#3 np.random.randint  或者　random.randint 
random.randint()的函数原型为：random.randint(a, b)  等价与　random.randrange(a,b+1,1)
用于生成一个指定范围内的整数
其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b

#4 random.randrange
random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数
如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数
random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效
random.randrange(10) 产生一个10范围内的整数
#5 np.random.choice 或者random.choice
random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)
参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型  list, tuple 字符串都属于sequence

print random.choice(["JGood", "is", "a", "handsome", "boy"])  
print random.choice(("Tuple", "List", "Dict")) 

#6 np.random.shuffle 或者 random.shuffle
random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱
如:
p = ["Python", "is", "powerful", "simple", "and so on..."]  
random.shuffle(p)  

#7 random.sample (获取指定列表的样本)
random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断 sample函数不会修改原有序列

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
print slice  
print list #原有序列并没有改变




