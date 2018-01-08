#使用pyplot模块　
#     plot画折线图　scatter画离散点图 hist画直方图　bar画条形图　pie画饼状图
#     show()显示图形　savefig()保存图形　figure() 调整图表的宽度　高度　用于画图之前
#     颜色映射　c=映射轴; cmap=plt.cm.颜色;
#     plt.axes().get_xaxis().set_visible(False)　隐藏坐标抽
import matplotlib.pyplot as plt
squares = [i**2 for i in range(10)]

#plot折线图
plt.plot(squares,linewidth=6)

plt.xlabel("x",fontsize=14)
plt.ylabel("y",fontsize=20)
plt.title("title",fontsize=30)

#plt.axis([xmin,xmax,ymin,ymax])　定义刻度标记的数值大小

#plt.tick_params()  定义刻度标记的形状大小 (标记的数字或者字母的形状大小)
plt.tick_params(axis='both',labelsize=30)

#隐藏坐标轴
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()


#scatter 离散点  s=100 定义点的大小
x=[1,2,3,4,5,6]
y=[1,2,4,3,6,5]
#删除默认点　蓝色黑边的黑边　edgecolor='none'
#更改点的颜色　c='red'
plt.scatter(x,y,c='red',edgecolor='none',s=1000)
plt.show()

#使用颜色映射　cmap=plt.cm.颜色   　大的值颜色深　小的值颜色浅　参考映射轴
#将c定义为映射的轴
plt.scatter(x,y,c=y,cmap=plt.cm.Reds,edgecolor='none',s=1000)
plt.show()

#保存图形　bbox_inches='tight' 删除多余空白区域
#plt.savefig('名称'，bbox_inches='tight')
