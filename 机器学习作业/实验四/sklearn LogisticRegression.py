import numpy as np
from sklearn.linear_model import LinearRegression
from numpy import *
import matplotlib.pyplot as plt


	
def loadDataSet():   # �������ݼ�
    dataMat = []  # ���������б�
    labelMat = []  # ������ǩ�б�
    fr = open('train_.txt')  # �򿪲��������ļ�
    for line in fr.readlines():  # ��ȡ�ļ�ÿһ��
        lineArr = line.strip().split()  # ��ȥÿһ�еĿո���ֳ��б�
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  # �������б�[1.0,lineArr��һ��Ԫ�أ�float��,lineArr�ڶ���Ԫ�أ�float��]
        labelMat.append(int(lineArr[2]))  # ���Ԫ�أ�Ԫ����Դ�� lineArr�б�ĵ�����Ԫ�أ�transform str to int first��         
    return dataMat, labelMat  


def sigmoid(inx):
    return 1.0/(1 + np.exp(- inx))
 
 

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.01
    maxCycles = 500
    theta = ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * theta)
        error = (labelMat + h)
        theta = theta - alpha * dataMatrix.transpose() * error
    return theta

def plotBestFit(theta):
    dataMat,labelMat = loadDataSet()
    dataArr =array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
   
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(xcord1, ycord1, s = 30, c = 'red', marker='s')
    ax.scatter(xcord2, ycord2, s = 30, c = 'blue')
    
    x = arange(0, 10.0, 0.5)
   
    y = (-theta[0] - theta[1] * x) / theta[2]
    ax.plot(x, y.T)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
dataMat,labelMat = loadDataSet()
theta = gradAscent(dataMat,labelMat)
plotBestFit(theta)