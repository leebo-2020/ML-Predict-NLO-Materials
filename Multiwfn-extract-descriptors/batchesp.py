#!/usr/bin/python3 -u
import os,  time
with open('calesp.sh', 'w') as oupt :
    oupt.write('#!/bin/bash\n')
    oupt.write('cat << EOF > $2-tmp-esp.txt\n')
    oupt.write('1000\n')
    oupt.write('10\n')
    oupt.write('16\n')
    oupt.write('12\n')
    oupt.write('0\n')
    oupt.write('EOF\n')
    oupt.write('Multiwfn  $1 < $2-tmp-esp.txt >> $2-esp.txt\n')
    oupt.write('rm ./$2-tmp-esp.txt\n')

# To read input file
tasks = [ ]
dir_lists = os.listdir(os.path.abspath('.'))
for sub_list in dir_lists :
    names = os.path.splitext(sub_list)
    if os.path.exists(names[0] + '-esp.txt') : 
        continue
    else :
        if names[1] == '.fchk' or names[1] == '.molden':
            tasks.append(sub_list)

# To enter main program
if __name__ == '__main__' :
    for sub_task in tasks :
        # To submit task
        fns = os.path.splitext(sub_task)
        os.system('bash calesp.sh %s %s' %(sub_task, fns[0]))
        # To judge task if finishing    
        status = False
        while not status :
            if not os.path.exists(fns[0] + '-tmp-esp.txt') :
                status= True
            else : 
                time.sleep(1)
        #os.system('mv %s %s'%('molden-esp.txt', fns[0]+ '-esp.txt'))
    if os.path.exists('nohup.out') : os.system('rm nohup.out')          

