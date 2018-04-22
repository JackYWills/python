import pickle
import nester
new_man=[]
try:
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('File error:'+str(perr))
nester.print_lol(new_man)
