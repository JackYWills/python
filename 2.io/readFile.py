#coding=utf-8
import os
os.getcwd()
os.chdir ('f:/python/io')
'''可使用try except代替if
if os.path.exists('sketch.txt'):'''
try:
    data = open('sketch.txt')
    print(data.readline(),end='')
    data.seek(0)
    for each_line in data:
        try:
            #if each_line.find(':') != -1:
                #直接打印
                '''print(each_line,end='')'''
                #分割加said后打印
                (role,line_spoken) = each_line.split(':',1)
                print(role,end='')
                print(' said: ',end='')
                print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
#else:
except IOError:
    print("未查找到文件！")

