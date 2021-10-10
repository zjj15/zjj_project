#把数据库里的表导入进excel里
#1、存在excel 2、连接数据库 3、把数据库里的表读出、写入进excel里


import xlwt
import pymysql
from xlwt.Workbook import Workbook

#连接数据库 ConnectMysql():
try:
    db=pymysql.connect(host='localhost',
    user='root',passwd='root',db='day1_createsql',
    charset='utf8'
    )
except:
    print("db disconnect !")
    
    
#打开文件
try:
   workboot=xlwt.Workbook('c.xlsx')
except:
    print("open C.xlsx failed！")
    #sheet=file.sheet_by_index(0)

#Workbook=xlwt.Workbook()
sheet=workboot.add_sheet('table_2')
print('sheet add successful')

    
#导出数据
def ExportTable():
    cursor=db.cursor()
    sql='select * from table_2'
    cursor.execute(sql)
    
    row=cursor.fetchone()#一行
    _len=len(row)
    i=0
    while(row):
        for j in range(0,_len):
            sheet.write(i,j,str(row))
            #sheet.write(i,j,str(row[j]).encode('latin-1').decode('gbk'))#utf8
            #sheet.write(i,j,str(row[j]))
            print(str(row))
            i+=1
            row=cursor.fetchone()
    db.commit()
    print("export table_1 data to excel!")
    workboot.save('c.xlsx')
    cursor.close()
    db.close()


ExportTable()










