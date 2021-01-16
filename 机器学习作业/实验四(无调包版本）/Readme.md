组长: 华航苇
组员：杨凯杰
作业题目: 学习sigmoid函数和逻辑回归算法。将实验三.2中的样例数据用聚类的结果打标签{0，1}，并用逻辑回归模型拟合。
1. 学习并画出sigmoid函数
2. 设计梯度下降算法，实现逻辑回归模型的学习过程。
3. 根据给定数据（实验三.2），用梯度下降算法进行数据拟合，并用学习好的模型对(2,6)分类。
（对2,3实现有难度的同学，可以直接调用sklearn中LogisticRegression进行学习）  

函数说明:
	Sig  返回sigmoid函数的值  
	Regression_function 回归函数    
	Derivation 损失函数的导数  
	
调用库：
import math    
import matplotlib.pyplot as plt  
import numpy as np   

在使用实验三的聚合数据来源于曾俊雄  
https://github.com/HeyLancelot/Machine-Learning-Experiment/tree/main/  
在此致谢
