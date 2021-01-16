组长: 华航苇
组员： 杨凯杰
作业题目: 基于实验一中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：
1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2. 以5分为间隔，画出课程1的成绩直方图。
3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4. 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。

函数说明:
	expertment_1  来自于实验一的数据处理函数，用以获得清洗后的数据
	mean 用于求平均值
	
调用库：
from 实验一 import expertment_1
import math
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

在相关矩阵与混淆矩阵部分参考了 肖小恩同学(https://github.com/tiger-xiao31/Machine_Learning--experiment/tree/main)的部分内容在此致谢
