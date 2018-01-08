from matplotlib import pyplot as plt
import csv
from datetime import datetime 
import matplotlib.dates as mdates
filename = 'register.csv'
with open(filename) as f_object:
	reader = csv.reader(f_object)
	first_row = next(reader)  #reader 切换到下一行开始
	dates=[]
	time1=[]
	time2=[]
	for row in reader:
		#print(len(row))
		if row:
			#print(datetime.strptime(row[0],'%Y-%m-%d').date())
			current_date = datetime.strptime(row[0],'%Y-%m-%d').date()
			dates.append(current_date)
			#print(datetime.strptime(row[1],'%I:%M').time())
			current_time1 = datetime.strptime(row[1],'%I:%M')
			time1.append(current_time1)
			current_time2 = datetime.strptime(row[2],'%I:%M')
			time2.append(current_time2)
			#time.append(row[1])
#datetime.strptime(date_str, format) 将时间字符串转换为datetime对象

figure = plt.figure()
plt.plot(dates,time1,c='yellow',label= 'Neng neng',linewidth=3)
plt.plot(dates,time2,c='red',label= 'w-mm',linewidth=3)
plt.legend(loc='upper left')
#折线之间阴影部分
plt.fill_between(dates,time1,time2,facecolor='blue',alpha=0.3)

#配置横坐标　
#设置日期显示格式 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#设置日期间隔  以日为间隔
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#斜的日期标签
figure.autofmt_xdate() 

#配置纵坐标 定义刻度范围
plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%I:%M'))
early = datetime.strptime('6:00','%I:%M')
late = datetime.strptime('11:30','%I:%M')
plt.ylim(early,late)

#定义坐标刻度大小
plt.tick_params(axis='both',labelsize=12)
#显示网格
plt.grid(True,linestyle = "-.",color = "blue",linewidth=2)  

#plt.text()可以在图中的任意位置添加文字说明

#plt.annotate()文本注释
#plt.annotate(' 2:00 begin sleep', xy=(datetime.strptime('2017-12-06','%Y-%m-%d'),
#datetime.strptime('10:24','%I:%M')), xytext=(datetime.strptime('2017-12-04','%Y-%m-%d'), datetime.strptime('10:40','%I:%M')),  
#arrowprops=dict(facecolor='red', shrink=0.05)) 
# 添加注释   第一个参数是注释的内容  xy设置箭头尖的坐标  xytext设置注释内容显示的起始位置  
# arrowprops 用来设置箭头  facecolor 设置箭头的颜色  headlength 箭头的头的长度  headwidth 箭头的宽度  width 箭身的宽度  



#设置样式
plt.title('Record of waking up',fontsize=25)
plt.xlabel('Date',fontsize=20)
plt.ylabel('AM-time',fontsize=20)

plt.scatter(dates,time1,c='yellow',marker='s',s=150)
plt.scatter(dates,time2,c='red',marker='^',s=150)
plt.show()


