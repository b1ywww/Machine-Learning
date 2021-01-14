############################
#                          #
#将两个表格的数据读入并且合并#
#                          #
############################
import xlrd
import xlwt

#读取Excel数据
def GetExcel(dir):
    data = xlrd.open_workbook(dir)
    table = data.sheet_by_name("Sheet1")
    rows = table.nrows
    col = table.ncols
    DataExcel = []
    dataExcel = {}
    for i in range(rows):
        DataExcel.append(table.row_values(i))
    for i in range(1, len(DataExcel)):
        n1 = int(DataExcel[i][0]) + 202000
        DataExcel[i][0] = str(n1)
        if(DataExcel[i][-1]=='bad'):
            DataExcel[i][-1]='1'
        elif(DataExcel[i][-1]=='general'):
            DataExcel[i][-1]='2'
        elif(DataExcel[i][-1]=='good'):
            DataExcel[i][-1]='3'
        elif(DataExcel[i][-1]=='excellent'):
            DataExcel[i][-1]='4'
        x = {DataExcel[i][0]: DataExcel[i][1:]}
        dataExcel.update(x)
    return dataExcel

#读取txt中数据
def GetTxt(dir):
    file = open(dir)
    dataTxt = []
    DataTxt = {}
    while 1:
        line = file.readline()
        line = line[:-1]
        if not line:
            break
        line = line.split(",")
        if (line[-1] == 'bad'):
            line[-1] = '1'
        elif (line[-1] == 'general'):
            line[-1] = '2'
        elif (line[-1] == 'good'):
            line[-1] = '3'
        elif (line[-1] == 'excellent'):
            line[-1] = '4'
        if(not line[0] in DataTxt.keys()):
            x = {line[0]:line[1:]}
            DataTxt.update(x)
        else:
            for i in range(1,16):
                if(DataTxt[line[0]][i-1] ==''):
                    DataTxt[line[0]][i-1] = line[i]
    file.close()
    return DataTxt

#合并TXT以及Execl数据
def dataMerge():
    dataExcel = GetExcel("D:/11.xlsx")
    dataTxt = GetTxt("D:/11.txt")
    dataALl = {}
    dataALl = dataTxt;
    for key in dataALl.keys():
        for i in range(0,15):
          if(not i == 13):
                if(key in dataExcel.keys()):
                   if(dataALl[key][i]==''):
                        if(not dataExcel[key][i] =='' ):
                            dataALl[key][i] = dataExcel[key][i]
                    #dataALl.update("{{}:{}}".format(key,dataExcel[key]))
    for key in dataExcel.keys():
        if(not key in dataALl):
            x = "{'" + "{}':{}".format(key, dataExcel[key])+"}"
            x = eval(x)
            dataALl.update(x)
    for key in dataTxt.keys():
        if(not key in dataALl):
            dataALl.update(dataTxt[key])

    for key in dataALl.keys():
        for i in range(0,15):
            if(not i == 13):
                if (key in dataTxt.keys()):
                    if(dataALl[key][i]==''):
                        if(not dataTxt[key][i] ==''):
                            dataALl[key][i] = dataTxt[key][i]
    return  dataALl
#将合并的数据写入excel
'''
def writeExcel(dataALl):
    workbook = xlwt.Workbook(encoding = 'utf-8')

    worksheet = workbook.add_sheet('My Worksheet')

    i = 1;
    for key in dataALl.keys():
        worksheet.write(i, 0, label=key)
        for k in range(15):
            worksheet.write(i, k+1, label=dataALl[key][k])
        i = i+1

    workbook.save('Excel_test.xls')
'''