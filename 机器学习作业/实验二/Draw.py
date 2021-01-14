import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from 实验一 import expertment_1
import math
import seaborn as sn
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd

def mean(a):
    sum = 0;
    for i in range(len(a)):
        sum = sum+a[i]
    return sum/(len(a)+1)
dataAll = expertment_1.dataMerge()

datax=[]
datay=[]
Hisx = [60,65,70,75,80,85,90,95,100];
Hisy = [0,0,0,0,0,0,0,0,0];
#绘制散点图的x坐标与y坐标
for key in dataAll.keys():
    if(dataAll[key][4]==''):
        dataAll[key][4] ='0'
    if(dataAll[key][-1]==''):
        dataAll[key][-1] ='0'
    if(not key == 'ID'):
        datax.append(int(dataAll[key][4]))
        datay.append(int(dataAll[key][-1]))
        for m in range(len(Hisx)):
            if(int(dataAll[key][4])>Hisx[m-1] and int(dataAll[key][4])<=Hisx[m]):
                Hisy[m] = Hisy[m] + 1
#绘制散点图以及课程1的散点图
fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax.scatter(datax, datay)
ax2.bar(Hisx, Hisy,width=4,linewidth=1.5, )
plt.show()




dataAll = expertment_1.dataMerge()
dataCn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dataC11 = 0
dataAk = []
dataBk = []
datastdA = [0, 0, 0, 0, 0, 0, 0, 0, 0]
datastdB = 0

#计算平均值
for i in range(4, 13):
    for key in dataAll.keys():
        if (dataAll[key][i] == ''):
            dataAll[key][i] = '0'
        if (dataAll[key][-1] == ''):
            dataAll[key][-1] = '0'
        if (not key == 'ID'):
            dataCn[i - 4] = dataCn[i - 4] + int(dataAll[key][i])
            if(i == 12):
                dataC11 = dataC11 + int(dataAll[key][-1])
for i in range(4, 13):
    dataCn[i - 4] = dataCn[i - 4] / (len(dataAll) - 1)

dataC11 = dataC11 / (len(dataAll) - 1)
dataCn.append(dataC11)

#归一化
for i in range(4, 13):
    for key in dataAll.keys():
        if (dataAll[key][i] == ''):
            dataAll[key][i] = '0'
        if (not key == 'ID'):
            datastdA[i-4] = datastdA[i-4]+ (float(dataAll[key][i]) - dataCn[i - 4]) ** 2
for key in dataAll.keys():
    if (not key == 'ID'):
        datastdB = round(datastdB + (float(dataAll[key][-1]) - dataC11) ** 2, 2)
datastdB = math.sqrt(datastdB / (len(dataAll) - 1))
for i in range(4, 13):
    datastdA[i-4] = round(math.sqrt(datastdA[i - 4] / (len(dataAll) - 2)), 2)

for key in dataAll.keys():
    if (not key == 'ID'):
        dataAll[key][-1] = (float(dataAll[key][-1]) - dataC11) / datastdB
        for i in range(4,13):
            dataAll[key][i] = (float(dataAll[key][i]) - dataCn[i-4])/datastdA[i-4]

stu_score = []#存储学生成绩
z = []#相关系数矩阵
ID = []
#计算相关系数矩阵
for key in dataAll.keys():
    if(not key == 'ID'):
        del dataAll[key][-2]
        x = []
        ID.append(key)
        for i in range(4,14):
            x.append(dataAll[key][i])
        stu_score.append(x)

std = []
for i in range(len(stu_score)):
    sum = 0
    for k in range(len(stu_score[i])):
        sum = sum + (stu_score[i][k]-mean(stu_score[i]))**2
    std.append(math.sqrt(sum/9))


for i in range(len(stu_score)):
    sum = 0;
    zz = []
    for j in range(len(stu_score)):
        for k in range(len(stu_score[i])):
            sum = sum + (stu_score[i][k] - mean(stu_score[i]))*(stu_score[j][k]-mean(stu_score[j]))
        zz.append(round((sum/9)/(std[i]*std[j]),3))
        sum = 0
    z.append(zz)
confusion_matrix=z
df_cm=pd.DataFrame(confusion_matrix)
sn.heatmap(df_cm,vmax=1,vmin=-1)
plt.show()

for i in range(len(z)):
    print(z[i])

#根据相关矩阵，找到距离每个样本最近的三个样本
max = [0,0,0]
max_line = []
max_ID = []
for i in range(len(z)):
    x = []
    for j in range(len(z[i])):
        if(i!=j and abs(z[i][j])>abs(max[0])):
            z[i][j] = abs(z[i][j])
            max[0] = z[i][j]
            max.sort()
    max_line.append(z[i].index(max[0]))
    max_line.append(z[i].index(max[1]))
    max_line.append(z[i].index(max[2]))
    x.append(ID[max_line[0]])
    x.append(ID[max_line[1]])
    x.append(ID[max_line[2]])
    max_ID.append(x)
    x = []
    max_line = []
    max = [0,0,0]

with open(r'D:\ID.txt', 'w') as f:
    for i in range(len(max_ID)):
        for j in range(3):
            f.write(max_ID[i][j])
            f.write('\t')
        f.write('\n')
    f.close()