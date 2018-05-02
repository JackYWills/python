#coding=utf-8

#1、定义字典的两种方式
cleese={}
print(type(cleese))

plain=dict()
print(type(plain))

#2、增加数据(不维护顺序)
#初始化
palin={'Name':'Michael Palin','Occupations':['comedian','tv']}
#动态新增：字符串、列表
cleese['Name']='John Cleese'
cleese['Occupations']=['actor','writer']

#3、查询
print(palin['Name'])
print(cleese['Occupations'][-1])

print(cleese)
print(palin)


