import matplotlib.pyplot as plt
import  Randwalk
while True:
    #更该类的形参 增加数据点
    rw = Randwalk.RandWalk(5000)
    rw.fill_walk( )
    #使用figure函数调整图像尺寸 尺寸大小是一个元组 放在绘制图像的最前面
    fig = plt.figure(figsize=(10, 6))
    point_num = list(range(rw.num_point))
    #利用图像映射需要一个列表和一个映射颜色        凸出点的轨迹根据列表c=point_num    cmp属性用来指定颜色
    plt.scatter(rw.x_value, rw.y_value, c=point_num, cmap=plt.cm.Greens, s=20)
    #绘制开始点和结束点
    plt.scatter(rw.x_value[0], rw.y_value[0], color='red')
    plt.scatter(rw.x_value[-1], rw.y_value[-1], color='red')
    #隐藏坐标轴的办法  get_xaxis  get_yaxis 的办法
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    #无限循环随机漫步
    answer = input("Do you stop(y/n)?")
    if answer == 'y':
        break







