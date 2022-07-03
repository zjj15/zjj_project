#字符串
#python没有字符之说，只有字符串

str1='i love sea'
str2=str1[:6]+' hello'+str1[6:]
str3=str1

print(str1)
print(str2)
print(str3)


#字符串函数
str4=str2.capitalize()#首字母大写
print(str4)

str5=str4.count('o')#计数
print(str5)

str6=str4.endswith('sea')#是否以 'sea'结尾
print(str6)

str7=str4.find('l')#find(str),检测 str 是否包含在字符串中,返回 第一个下标,如果没有则返回-1
print(str7)

str8=str4.index('l',3,15)#index(str,start,end),在start和end范围中查找str字符串，如果不存在产生异常
print(str8)

#补充：字符串比较函数 https://wenku.baidu.com/view/caec9c67bd1e650e52ea551810a6f524cdbfcb47.html

str9='123456'
str10='abcHG'
str11='123abcHG'
str12='123-abc&9*m'
str13='abcdef'
str14='中文'
str15='中文***'
print('--------isalnum-----------')
#至少有一个字符且字符都是数字或字母，则返回True
print(str9.isalnum())#true
print(str10.isalnum())#true
print(str11.isalnum())#true
print(str12.isalnum())#false
print(str13.isalnum())#true
print(str14.isalnum())#true  中文也算作字母*********
print(str15.isalnum())#false

print('--------isdigit-----------')
#至少有一个字符且所有字符都是数字，则返回True
print(str9.isdigit())#true
print(str10.isdigit())#false
print(str11.isdigit())#false
print(str12.isdigit())#false
print(str13.isdigit())#false
print(str14.isdigit())#false
print(str15.isdigit())#false

print('--------isalpha-----------')
#至少有一个字符且所有字符都是字母，则返回True
print(str9.isalpha())#false
print(str10.isalpha())#true
print(str11.isalpha())#false
print(str12.isalpha())#false
print(str13.isalpha())#true
print(str14.isalpha())#true 中文也算作字母*********
print(str15.isalpha())#false



print('--------islower-----------')
#全是小写
print(str9.islower())#false
print(str10.islower())#false
print(str11.islower())#false
print(str12.islower())#true,全部是小写，不管里面有啥
print(str13.islower())#true,全部是小写
print(str14.islower())#false
print(str15.islower())#false


print('--------isupper-----------')
#全是大写
str16='HHHLLLKKK'
print(str11.isupper())#false
print(str14.isupper())#中文汉字不存在大小写
print(str16.isupper())


#格式化 format
str17='{0} love {1} {2}'.format("JJ","w",'G')
print(str17)#JJ love w G

print('\\')#\

str18='{{0}}'.format("请输出")
print(str18)#{0}
str19='{0} {{0}}'.format("请输出")
print(str19)#请输出 {0}
str20='{0:.1f}{1}'.format(27.658,'GB')
print(str20)#27.7GB 1f四舍五入保留一位



#字符格式化符号
#%c 格式化字符及其asall码
a='%c %c %c' % (97,98,99)
print(a)#a b c


b='%c %c %c %c' % (97,98,99,100)
print(f'{b}')#a b c d

c=101
print('%c' %(c))#e
