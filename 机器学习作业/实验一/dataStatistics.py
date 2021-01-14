import expertment_1
import math
#问题一
def quirement_1():
    dataAll = expertment_1.dataMerge() # 读取清洗后的数据放入 dataAll
    dataBeijing = {}                   # 存储北京的数据dataBeijing
    data=[0,0,0,0,0,0,0,0,0,0,0]       #  平均值数组data

    #将北京的数据存入dataBeijing
    for key in dataAll.keys():
        if(dataAll[key][1] =="Beijing"):
            x = eval("{'" + "{}':{}".format(key, dataAll[key]) + "}")
            dataBeijing.update(x)

    #计算平均值并放入data
    for key in dataBeijing.keys():
        for i in range(4,15):
            if(not i == 13):
                data[i-4] = data[i-4]+int(dataBeijing[key][i])
    print("——————————问题一————————————")
    print("家在北京的成绩平均数为:")
    for i in range(4,15):
        data[i-4] = round(data[i-4]/len(dataBeijing),2)
        print(dataAll['ID'][i]+":"+str(data[i-4]))
#问题二
def quirement_2():
    dataAll = expertment_1.dataMerge()
    dataGuangzhou = {}
    sum = 0
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    #将广州数据放入dataGuangzhou
    for key in dataAll.keys():
        if (dataAll[key][1] == "Guangzhou"):
            x = eval("{'" + "{}':{}".format(key, dataAll[key]) + "}")
            dataGuangzhou.update(x)

    #计算总和
    for key in dataGuangzhou.keys():
        if(int(dataGuangzhou[key][4])>=80 and int(dataGuangzhou[key][12])>=9):
            sum = sum + 1
    print("——————————问题二————————————")
    print("学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量:"+str(sum))

#问题3
def quirement_3():
    dataAll = expertment_1.dataMerge()
    dataShanghai = 0
    sumShanghai = 0
    dataGuangzhou = 0
    sumGuangzhou = 0
    for key in dataAll.keys():
        if(dataAll[key][-1] == ''):
            dataAll[key][-1] = '0'
        if (dataAll[key][1] == "Guangzhou"):
            dataGuangzhou = dataGuangzhou+int(dataAll[key][-1])
            sumGuangzhou = sumGuangzhou + 1
        elif(dataAll[key][1] == "Shanghai"):
            dataShanghai = dataGuangzhou+int(dataAll[key][-1])
            sumShanghai = sumShanghai + 1
    print("——————————问题三————————————")
    print(dataShanghai)
    print(dataGuangzhou)
    if(dataGuangzhou > dataShanghai):
        print("广州地区强")
    elif(dataGuangzhou == dataShanghai):
        print("两个地区一样强")
    elif(dataGuangzhou < dataShanghai):
        print('上海地区强')

#问题4
def quirement_4():
    dataAll = expertment_1.dataMerge()
    dataCn=[0,0,0,0,0,0,0,0,0,0,0]
    dataC11 = 0
    dataAk = []
    dataBk = []
    datastdA = [0,0,0,0,0,0,0,0,0,0,0]
    datastdB = 0

    #将课程C1到C9的成绩总和放入dataCn，将体育课成绩总和放入dataC11
    for i in range(4,13):
        for key in dataAll.keys():
            if(dataAll[key][i]==''):
                dataAll[key][i] ='0'
            if (dataAll[key][-1] == ''):
                dataAll[key][-1]  = '0'
            if(not key == 'ID'):
                dataCn[i-4] = dataCn[i-4]+int(dataAll[key][i])
                dataC11 = dataC11 + int(dataAll[key][-1])

    #计算各课程平均值
    for i in range(4,13):
        dataCn[i-4] = dataCn[i-4]/(len(dataAll)-1)

    dataC11 = dataC11 / (len(dataAll) - 1)

    #计算C1到C9协方差
    for i in range(4,13):
        for key in dataAll.keys():
            if(dataAll[key][i]==''):
                dataAll[key][i] ='0'
            if (not key == 'ID'):
                datastdA[i-4] = datastdA[i-4]+(int(dataAll[key][i]) - dataCn[i-4])**2

    #计算C11协方差
    for key in dataAll.keys():
        if(not key == 'ID'):
            datastdB = round(datastdB+(int(dataAll[key][-1])-dataC11)**2,2)
    datastdB = math.sqrt(datastdB/(len(dataAll)-2))
    for i in range(4, 13):
        datastdA[i-4] = round(math.sqrt(datastdA[i-4]/(len(dataAll)-2)),2)
    print("——————————问题四————————————")
    for i in range(4,13):
        if(not i == 13):
            for key in dataAll.keys():
                if(not key == 'ID'):
                    a = (int(dataAll[key][i]) - dataCn[i-4])/datastdA[i-4] #计算ak
                    dataAk.append(a);
                    b = (int(dataAll[key][-1]) - dataC11)/datastdB #计算bk
                    dataBk.append(b)

            sum = 0
            for k in range(len(dataBk)):
                    sum = sum + dataBk[k]*dataAk[k]  #计算相关性
            print(dataAll['ID'][i]+"的相关性:"+str(sum))
            dataAk = []
            dataBk = []
quirement_1()
quirement_2()
quirement_3()
quirement_4()