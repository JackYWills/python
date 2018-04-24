#coding=utf-8
import os

os.chdir(os.getcwd()+'\data')

with open('james.txt') as jaf:
    data = jaf.readline()
james=data.strip().split(',')
print(sorted(james))

with open('julie.txt') as juf:
    data = juf.readline()
julie=data.strip().split(',')
print(sorted(julie))

with open('mikey.txt') as mif:
    data = mif.readline()
mikey=data.strip().split(',')
print(sorted(mikey))

with open('sarah.txt') as saf:
    data = saf.readline()
sarah=data.strip().split(',')
print(sorted(sarah))
