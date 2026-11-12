#!/usr/bin/python3 -u
import os, time
with open('calorbdipole.sh', 'w') as oupt :
    oupt.write('#!/bin/bash\n')
    oupt.write('cat << EOF > $2-tmp-orbdipole.txt\n')
    oupt.write('1000\n')
    oupt.write('10\n')
    oupt.write('16\n')
    oupt.write('200\n')
    oupt.write('10\n')
    oupt.write('1\n')
    oupt.write('4\n')
    oupt.write('EOF\n')
    oupt.write('Multiwfn  $1 < $2-tmp-orbdipole.txt\n')
    oupt.write('mv orbint.txt $2-orbint.txt\n')
    oupt.write('rm ./$2-tmp-orbdipole.txt\n')

# To read input file
tasks = [ ]
dir_lists = os.listdir(os.path.abspath('.'))
for sub_list in dir_lists :
    names = os.path.splitext(sub_list)
    if names[1] == '.fchk' or names[1] == '.molden':
        tasks.append(sub_list)

# To enter main program
if __name__ == '__main__' :
    for sub_task in tasks :
        # To submit task
        fns = os.path.splitext(sub_task)
        os.system('bash calorbdipole.sh %s %s' %(sub_task, fns[0]))
        # To judge task if finishing    
        status = False
        while not status :
            if not os.path.exists(fns[0] + '-tmp-orbdipole.txt') :
                status= True
            else : 
                time.sleep(3)
    if os.path.exists('nohup.out') : os.system('rm nohup.out')          

