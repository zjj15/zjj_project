#coding=UTF-8
#对excel操作
#基础用法：  https://www.jb51.net/article/152405.htm    https://www.jb51.net/article/60510.htm

#**1.打开一个指定的excel，然后读取里面存储的内容，以最后一个单元格的内容为界，
#**	打印出其所在的行号，列号，并且打印出其前面所有单元格的内容
#**2.创建一个新的excel表格，然后往里面写入一些东西

import xlrd
import xlwt

#1.打开excel表格
filename="BackUpData_CheckList_Base_test.xlsx"
workbook=xlrd.open_workbook(filename)

#2.读取ecxel表格的sheet
sheet=workbook.sheet_names()
print(sheet)

#3.获取需要的sheet,第2个sheet
sheet_need=workbook.sheet_by_index(1)

#4.获取sheet行列
row=sheet_need.nrows
col=sheet_need.ncols



#5.打印所有数据到指定文件中
file=xlwt.Workbook()
#6.创建sheet
sheet1=file.add_sheet('case_path')

#7.从第一个文档里读取内容
i=0
j=0
for i in range(row):
    for j in range(col):
        cell=sheet_need.cell(i,j).value
        print(cell)
        #8.写入内容
        sheet1.write(i,j,cell,xlwt.XFStyle())


file.save('b.xlsx')
