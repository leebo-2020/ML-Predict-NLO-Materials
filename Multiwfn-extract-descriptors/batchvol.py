#!/usr/bin/python3 -u
import os, time

with open('calvol.sh', 'w') as oupt :
    oupt.write('#!/bin/bash\n') 
    oupt.write('cat << EOF > ${2}-volcalcall.txt\n') 
    oupt.write('1000\n') 
    oupt.write('10\n') 
    oupt.write('16\n') 
    oupt.write('12\n') 
    oupt.write('3\n') 
    oupt.write('0.15\n') 
    oupt.write('6\n') 
    oupt.write('EOF\n') 
    oupt.write('Multiwfn $1 < ${2}-volcalcall.txt | tee ${2}-vol.txt\n') 
    oupt.write('grep "Volume:" ./${2}-vol.txt |nl >> ${2}-vol-result.txt\n') 
    oupt.write('grep "Estimated density according to mass and volume (M/V):" $2-vol.txt|nl >> ${2}-vol-result.txt\n') 
    oupt.write('grep "Overall surface area:" $2-vol.txt|nl >> ${2}-vol-result.txt\n') 
    oupt.write('rm ./${2}-volcalcall.txt\n') 
    oupt.write('rm ./${2}-vol.txt\n') 

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
        os.system('bash calvol.sh %s %s' %(sub_task, fns[0]))
        # To judge task if finishing    
        status = False
        while not status :
            if not os.path.exists(fns[0] + '-volcalcall.txt') :
                status= True
            else : 
                time.sleep(3)
    if os.path.exists('nohup.out') : os.system('rm nohup.out')          

