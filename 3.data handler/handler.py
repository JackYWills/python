#coding=utf-8
import os

#格式化时间函数(-/:转换为.)
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

#读取txt文件为数组函数
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

os.chdir(os.getcwd()+'\data')

#将文件解析为数组
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
'''
with open('james.txt') as jaf:
    data = jaf.readline()
james=data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie=data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey=data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah=data.strip().split(',')
'''

#使用函数对数组做格式化处理（并去重取前三）
print(sorted(set([sanitize(t) for t in james])) [0:3])
print(sorted(set([sanitize(t) for t in julie])) [0:3])
print(sorted(set([sanitize(t) for t in mikey])) [0:3])
print(sorted(set([sanitize(t) for t in sarah])) [0:3])
'''
#未去重取前三：
clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]
'''
'''
#未使用列表推导：
clean_james=[]
for each_t in james:
    clean_james.append(sanitize(each_t))
    
clean_julie=[]
for each_t in julie:
    clean_julie.append(sanitize(each_t))
    
clean_mikey=[]
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
    
clean_sarah=[]
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))
'''


