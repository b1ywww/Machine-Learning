import math
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

def Sig(x):
    y = math.exp(x) / (math.exp(x) + 1)
    if y >= 0.5:
        return 1
    else:
        return 0
x = np.linspace(-10,10,100000)
sigmoid=[]#  math.exp(x)/(math.exp(x)+1)
for i in x:
    sigmoid.append(math.exp(i)/(math.exp(i)+1))
plt.figure() # 定义一个图像窗口
plt.plot(x, sigmoid) # 绘制曲线 y
plt.show()
#采用的是曾俊雄同学的聚类结果
data = {
    (3.45,7.08,1):0,
    (1.76,7.24,1):0,
    (4.29,9.55,1):0,
    (3.35,6.65,1):0,
    (3.17,6.41,1):0,
    (3.68,5.99,1): 0,
    (2.11,4.08,1): 0,
    (2.58,7.10,1): 0,
    (3.45,7.88,1): 0,
    (6.17,5.40,1): 1,
    (4.20,6.46,1): 0,
    (5.87,3.87,1): 1,
    (5.47,2.21,1): 1,
    (5.87,3.62,1): 1,
    (5.47,2.21,1): 1,
    (5.97,3.62,1): 1,
    (6.24,3.06,1): 1,
    (6.89,2.41,1): 1,
    (5.38,2.32,1): 1,
    (5.13,2.73,1): 1,
    (7.26,4.19,1): 1,
    (6.32,3.62,1): 1,
}
#学习率
learn = 0.001
w = [0.5,0.5,0.5]
#回归函数
def Regression_function(w,x):
    return w[0]*x[0]+w[1]*x[1]+w[2]*x[2]
#导数
def Derivation(data,w,x):
    sum = 0
    for i in data.keys():
        sum += (Sig(Regression_function(w,i))-data[i])*i[x]
    return sum/(len(data)+1)

#开始训练
for i in range(1000):
    w[0]=w[0]-learn*Derivation(data,w,0)
    w[1]=w[1]-learn*Derivation(data,w,1)
    w[2]=w[2]-learn*Derivation(data,w,2)

#绘制分类函数
a = w[0]/w[1]
b = w[2]/w[1]
y = []
x = np.linspace(0,10,100000)
for i in x:
    y.append(-a*i-b)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
datax = []
datay = []
for i in data.keys():
    datax.append(i[0])
    datay.append(i[1])
ax.scatter(datax, datay)
ax.plot(x,y)
plt.show()
print("(2,6)属于:")
print(Sig(Regression_function(w,(2,6,1))))