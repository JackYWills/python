#coding=utf-8
import nester
man=[]
other=[]
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('文件丢失！')
try:
    #man_file=open('man_data.txt','w')
    #other_file=open('other_data.txt','w')
    with open('man_data.txt','w') as man_file,open('other_data.txt','w') as other_file:
        nester.print_lol(man,fn=man_file)
        nester.print_lol(man,fn=other_file)
except IOError as err:
    print('File error:'+str(err))
'''finally:
    man_file.close()
    other_file.close()'''
