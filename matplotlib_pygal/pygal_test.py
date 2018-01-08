#可视化包pygal
#生成矢量化的文件
# 绘制柱状图
#导入可视化pygal包
import pygal
from pygal_ import SeZi
#新建2个骰子类
sezi1 = SeZi()
sezi2 = SeZi()
#模拟1000次存放结果
results = []
for rollnumber in range(1000):
    result = sezi1.roller() + sezi2.roller()
    results.append(result)
print(results)

#计算结果的频率
frequencies = []
for value in range(2,sezi1.number_sides+sezi2.number_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#生成可视化的柱状图
hist = pygal.Bar()
hist.title ='results of rolling 1000 times'

#横坐标的标签以及标题
hist.x_label = [2,3,4,5,6,7,8,9,10,11,12]
hist.x_title = 'results'
#纵坐标的标题     函数add（）参数1表示一个标签 参数2 一个列表（一般对应的 Y 值）  调用一次指定一个颜色
hist.y_title = 'frequency of result'
hist.add('sezi1+sezi2',frequencies[:3]) #频率是从小到大的  前3个颜色一类
hist.add('sezi1+sezi2',frequencies[3:])#频率是从小到大的  后面一类

#生成文件  svg格式  在浏览器内打开
hist.render_to_file('pygal_test.svg')

