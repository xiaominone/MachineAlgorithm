#模块pygal 画矢量图形
#画条形图Bar()　需要知道一个频数列表　用于表示y轴
#                          x_labels＝列表　表示x轴刻度　　字符串形式
import pygal

frequencies=[3,2,4,8,12,22]
hist = pygal.Bar()      # 生成实例

hist.title = 'Results of rolling one D6 1000 times'  # 标题
hist.x_labels = ['1','2','3','4','5','6']           # X轴数值坐标
hist.x_title = 'Result'                                 # X轴标题

hist.y_title = 'Frequency of Result'                # Y轴标题

#add 传入Y轴数据 
hist.add('D6',frequencies)
