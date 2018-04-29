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

#读取txt文件为字典，并格式化时间
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp_data = data.strip().split(',')        
        return({'Name':temp_data.pop(0),
                'DOB':temp_data.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in temp_data]))[0:3])})
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

os.chdir(os.getcwd()+'\data')

james = get_coach_data('james2.txt')
print(james['Name']+"'s fastest times are:"+james['Times'])

julie = get_coach_data('julie2.txt')
print(julie['Name']+"'s fastest times are:"+julie['Times'])

mikey = get_coach_data('mikey2.txt')
print(mikey['Name']+"'s fastest times are:"+mikey['Times'])

sarah = get_coach_data('sarah2.txt')
print(sarah['Name']+"'s fastest times are:"+sarah['Times'])


