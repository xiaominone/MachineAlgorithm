#Python�е�numpy.randomģ��  ������������� 
#random.�����������ߡ���np.random.������������ע��ʹ�÷�����



#0 np.random.rand()  �������ȷֲ�������ֵ 0-1��Χ�� ֻ����һά���� ����������Ӧ��Χ
 eg ��np.random.rand(4) ����4��0-1��Χ�ڵ�ֵ
#  binomial ��������ֲ�������ֵ  beta  Beta�ֲ�������ֵ   gamma  ٤��ֲ�����ֵ

#1 np.random.random
np.random.random(4)  #����4��0-1��Χ�ڵ�ֵ
np.random.random(size=(2,2))#0 <= n < 1.0 2*2���������
np.random.rand(2,2) #0 <= n < 1.0 2*2���������
#2 np.random.uniform�����ߡ�random.uniform
random.uniform�ĺ���ԭ��Ϊ��random.uniform(a, b)
��������һ��ָ����Χ�ڵ������������
������������һ�������ޣ�һ�������ޡ����a > b�������ɵ������n: a <= n <= b ��� a <b�� �� b <= n <= a
1 ����Ϊ��Ĭ������һ��[0,1)���ȷֲ���ֵ 
2 ����Ϊ1����ʱ��  uniform(a)   ����һ��[0,a)���ȷֲ���ֵ

#3 np.random.randint  ���ߡ�random.randint 
random.randint()�ĺ���ԭ��Ϊ��random.randint(a, b)  �ȼ��롡random.randrange(a,b+1,1)
��������һ��ָ����Χ�ڵ�����
���в���a�����ޣ�����b�����ޣ����ɵ������n: a <= n <= b

#4 random.randrange
random.randrange�ĺ���ԭ��Ϊ��random.randrange([start], stop[, step])����ָ����Χ�ڣ���ָ�����������ļ����� ��ȡһ�������
�磺random.randrange(10, 100, 2)������൱�ڴ�[10, 12, 14, 16, ... 96, 98]�����л�ȡһ�������
random.randrange(10, 100, 2)�ڽ������ random.choice(range(10, 100, 2) ��Ч
random.randrange(10) ����һ��10��Χ�ڵ�����
#5 np.random.choice ����random.choice
random.choice�������л�ȡһ�����Ԫ�ء��亯��ԭ��Ϊ��random.choice(sequence)
����sequence��ʾһ���������͡�����Ҫ˵�� һ�£�sequence��python����һ���ض������ͣ����Ƿ�ָһϵ�е�����  list, tuple �ַ���������sequence

print random.choice(["JGood", "is", "a", "handsome", "boy"])  
print random.choice(("Tuple", "List", "Dict")) 

#6 np.random.shuffle ���� random.shuffle
random.shuffle�ĺ���ԭ��Ϊ��random.shuffle(x[, random])�����ڽ�һ���б��е�Ԫ�ش���
��:
p = ["Python", "is", "powerful", "simple", "and so on..."]  
random.shuffle(p)  

#7 random.sample (��ȡָ���б������)
random.sample�ĺ���ԭ��Ϊ��random.sample(sequence, k)����ָ�������������ȡָ�����ȵ�Ƭ�� sample���������޸�ԭ������

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
slice = random.sample(list, 5)  #��list�������ȡ5��Ԫ�أ���Ϊһ��Ƭ�Ϸ���  
print slice  
print list #ԭ�����в�û�иı�




