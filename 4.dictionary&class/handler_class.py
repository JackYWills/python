#coding=utf-8
import os

#Athlete类记录选手信息
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        #self.top3_times = top3(self) #:增加该字段会降低灵活性

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self,add_time):
        self.times.append(add_time)

    def add_times(self,add_times):
        self.times.extend(add_times)
        '''for t in add_times:
            self.times.append(t)'''   
        
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

#读取txt文件为Athlete对象，并格式化时间
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp_data = data.strip().split(',')        
        return Athlete(temp_data.pop(0),temp_data.pop(0),temp_data)
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

os.chdir(os.getcwd()+'\data')

james = get_coach_data('james2.txt')
james.add_time('1.02')
james.add_times(['1-01','2.01'])
print(james.name+"'s fastest times are:"+str(james.top3()))

'''
julie = get_coach_data('julie2.txt')
print(julie['Name']+"'s fastest times are:"+julie['Times'])

mikey = get_coach_data('mikey2.txt')
print(mikey['Name']+"'s fastest times are:"+mikey['Times'])

sarah = get_coach_data('sarah2.txt')
print(sarah['Name']+"'s fastest times are:"+sarah['Times'])
'''

