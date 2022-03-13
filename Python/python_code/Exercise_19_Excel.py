#coding=utf-8
#python对Excel进行操作
#参照博客https://www.cnblogs.com/zeke-python-road/p/8986318.html
from  openpyxl import Workbook
from  openpyxl import load_workbook
import time

name='python_excel_1.xlsx'
name2='python_excel_2.xlsx'
#1.新建Excel文件并保存;
#每个workbook创建后，会默认创建一个sheet
wb=Workbook()
wb.save(name)
print('creat successful')

#2.写入
ws=wb.active
#print(ws)#<Worksheet "Sheet">
ws['A1']='hello everybody it\'s my pleasure to show some of you that my diary about my life recently'
ws['A2']=time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime())
wb.save(name)

#3.读取
wb2=load_workbook(name)
#<openpyxl.workbook.workbook.Workbook object at 0x10e92d890>
ws2=wb2.active #<Worksheet "Sheet">
row=[]
for row in ws2.iter_rows():
    print(row[0].value)#hello everybody it's my pleasure to show some of you that my diary about my life recently
    print('\n')        #2022年03月06日 19时36分07秒

wb2.save(name2) 

#4.批量新建工作簿
for i in range(3,13):
    wb=Workbook()
    wb.save('python_excel_'+ (str)i +'.xlsx')


#.创建sheet
ws1=wb.create_sheet('Mysheet1')
ws1.title='Mysheet1'
ws.sheet_properties.tabcolor='1072ba'
wb.save(name)