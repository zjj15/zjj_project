#字典 Dictionary;映射类型
dict1={'猫':'吃鱼', '狗':'吃肉','兔子':'吃草','老鼠':'吃汉堡','猪八戒':'吃蝴蝶' }
dict2={1:'book',2:'ruler',3:'eye',4:'flyb',5:'map'}
dict3={9:'wbook',2:'mruler',1:'keye',2:'hflyb',7:'emap'}
dict4=dict((('A',96),('B',97),('C',98),('D',99)))#{'D': 99, 'B': 97, 'C': 98, 'A': 96},为啥这么多括号，因为dict只有一个参数
dict5=dict(小甲鱼='emm',网站=2)#dict5:    {'网站': 2, '小甲鱼': 'emm'}
dict5['小甲鱼']='修改后'
print(dict5)#{'小甲鱼': '修改后', '网站': 2}
dict5['hello']='okk'
print(dict5)#dict5:    {'小甲鱼': '修改后', 'hello': 'okk', '网站': 2}
dict6={}



print('dict1:   ',dict1)
print('dict1:   ',dict1['猫'])#dict1:    吃鱼
print('dict2:   ',dict2[2])
print('dict3:   ',dict3[2])#dict3:    hflyb ,打印h开头的而不是m开头的
print('dict4:   ',dict4)#dict4:    {'C': 98, 'D': 99, 'A': 96, 'B': 97}
print('dict5:   ',dict5)#dict5:    {'小甲鱼': '修改后', 'hello': 'okk', '网站': 2}
print('dict6:   ',dict6)#dict6:    {}




#2.内建函数
#2.1 fromkeys()创建并返回一个新的字典
dict7={}
print(dict7.fromkeys((1,2,3)))#{1: None, 2: None, 3: None}
print(dict7.fromkeys((1,2,3),'Number'))#{1: 'Number', 2: 'Number', 3: 'Number'}
print(dict7.fromkeys((1,2,3),('Number1','Number2','Number3')))
#{1: ('Number1', 'Number2', 'Number3'), 2: ('Number1', 'Number2', 'Number3'), 3: ('Number1', 'Number2', 'Number3')}
print(dict7.fromkeys((range(10)),'Number'))
#{0: 'Number', 1: 'Number', 2: 'Number', 3: 'Number', 4: 'Number', 5: 'Number', 6: 'Number', 7: 'Number', 8: 'Number', 9: 'Number'}


dict8=dict.fromkeys((range(5)),'data')
for eachkey in dict8.keys():
    print('keys: ', eachkey)
'''
keys:  0
keys:  1
keys:  2
keys:  3
keys:  4
'''

for eachkey in dict8.values():
    print('values: ', eachkey)
'''
values:  data
values:  data
values:  data
values:  data
values:  data
'''
for eachkey in dict8.items():
    print('item: ', eachkey)

'''
item:  (0, 'data')
item:  (1, 'data')
item:  (2, 'data')
item:  (3, 'data')
item:  (4, 'data')
'''
#2.2 get(key)
print(dict8.get(3))#data
print(dict8.get(5, 'num'))
print(2 in dict8)#True
print(6 in dict8)#False
print('data' in dict8)#False 为啥会false，因为 in关键字用在字典里是查找key而不是values


#清空字典 clear
print(dict7)#{}
print(dict7.clear())#None


#copy 浅拷贝
a={1:'one',2:'two'}
b=a.copy()
c=a
print(a)#{1: 'one', 2: 'two'}
print(b)#{1: 'one', 2: 'two'}
print(c)#{1: 'one', 2: 'two'}
print(id(a))#1913661700744
print(id(b))#1913661700552
print(id(c))#1913661700744