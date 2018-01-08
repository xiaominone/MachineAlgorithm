import matplotlib.pyplot as plt
# matplotlib模块 导入模块pyplot 并重新命名 plt
squres = [1,4,9,16]
#线段宽度             离散点 scatter
plt.plot(squres, linewidth=5, color='black')#横坐标是从小0开始
plt.plot([1,2,3,4], squres, linewidth=5,c='red')#自定义横坐标
#绘制离散点
plt.scatter(3, 3, s=200, color='red')# 单个离散点 （x,y） s设置大小为200
plt.scatter([2,2,2,2,2],[1,2,3,4,5])#多个离散点 采用列表 自定义横纵坐标
#坐标标题
plt.title('squre number', fontsize=10)
#坐标名称和字体大小
plt.xlabel('value', fontsize='15')
plt.ylabel('squre value', fontsize=10)
#坐标范围
plt.axis([0,5,0,30])
#刻度上面标记数字的大小 tick_params
plt.tick_params(axis='both', labelsize=10)
plt.show()

#产生随机离散点  离散点之间颜色映射colormap即属性cmp  cmap=plt.cm.Blues  属性c指定参考列表   用颜色深浅区分值的大小
x_value = list(range(1, 11))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, edgecolors='red', c=y_value, cmap=plt.cm.Blues, s=200)
plt.show()

#保存图表 参数1 图表的名称 参数2 去除图表空白区域
plt.savefig('scatter_.png', bbox_inches='tight')
