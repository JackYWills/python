#coding=utf-8
import pickle
from athleteList import AthleteList

        
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
        return AthleteList(temp_data.pop(0),temp_data.pop(0),temp_data)
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name]=ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error(put_to_store):'+str(ioerr))
    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):'+str(ioerr))
    return (all_athletes)
'''
os.chdir(os.getcwd()+'\data')

james = get_coach_data('james2.txt')
james.append('1.02')
james.extend(['1-01','2.01'])
print(james.name+"'s fastest times are:"+str(james.top3()))
'''
