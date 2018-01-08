#可视化包pygal
#生成矢量化的文件
# 绘制柱状图
#模拟一个骰子
from random import randint
#模拟一个骰子
class SeZi():
    def __init__(self, number_sides=6):
        self.number_sides = number_sides

    def roller(self):
        return randint(1, self.number_sides)




