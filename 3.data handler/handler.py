#coding=utf-8
import os

#将文件解析为数组
os.chdir(os.getcwd()+'\data')

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

#格式化时间函数
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

#对数组做格式化处理
clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]
'''
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
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

