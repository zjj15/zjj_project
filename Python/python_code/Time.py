#coding=UTF-8
import time
#1.时间戳
print("时间戳：", time.time())
#时间戳： 1629207391.8821845

#2.获取当前时间
print("获取当前时间：", time.localtime(time.time()))
#获取当前时间： time.struct_time(tm_year=2021, tm_mon=8, tm_mday=17, tm_hour=21, tm_min=36, tm_sec=31, tm_wday=1, tm_yday=229, tm_isdst=0)

#3.获取格式化时间
print("获取格式化时间: ", time.asctime(time.localtime(time.time())))
#获取格式化时间:  Tue Aug 17 21:36:31 2021

#4.获取格式化日期
print("获取格式化日期：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
#获取格式化日期： 2021-08-17 21:36:31
