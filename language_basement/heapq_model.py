import math 
import random
import io
import heapq as hq 
def show_tree(tree, total_width=36, fill=' '):
   output = io.StringIO()
   last_row = -1
   for i, n in enumerate(tree):
     if i:
       row = int(math.floor(math.log(i+1, 2)))
     else:
       row = 0
     if row != last_row:
       output.write('\n')
     columns = 2**row
     col_width = int(math.floor((total_width * 1.0) / columns))
     output.write(str(n).center(col_width, fill))
     last_row = row
   print(output.getvalue())
   print ('-' * total_width)
   print
   return
 
data = random.sample(range(1,8), 7)
print ('data: ', data)
show_tree(data)

print ('-' * 36)

#heapq.heapify(list)将list类型转化为heap, 在线性时间内, 重新排列列表
hq.heapify(data)
show_tree(data)

print ('-' * 36)

#heapq.heappush(heap, i)　将一个一个元素添加到堆中
heap = []
data = random.sample(range(1,8), 7)
print('data: ' )
print(data)
for i in data:
	print ('add ' + str(i))
	hq.heappush(heap, i)
	show_tree(heap)

print ('-' * 36)
#删除并返回堆中最小的元素, 通过heapify() 和heappop()来排序
data = random.sample(range(1, 8), 7)
print ('data: ') 
print(data)
hq.heapify(data)
show_tree(data)
heap = []
while data:
	i = hq.heappop(data)
	print('pop :' + str(i))
	show_tree(data)
	heap.append(i)
print('heap:')
print(heap)
print ('-' * 36)
#heapq.heapreplace(iterable, n)删除现有元素并将其替换为一个新值。
data = random.sample(range(1, 8), 7)
print ('data: ')
print(data)
hq.heapify(data)
show_tree(data)
 
for n in [8, 9, 10]:
	smallest = hq.heapreplace(data, n)
	print ('replace ' + str(smallest) + ' with ' + str(n))  #(smallest, n)
	show_tree(data)

print ('-' * 36)	
#heapq.nlargest(n, iterable) 和 heapq.nsmallest(n, iterable)返回列表中的n个最大值和最小值
data = range(1,6)
l = hq.nlargest(3, data)
print(l)    
 
s = hq.nsmallest(3, data)
print(s)




