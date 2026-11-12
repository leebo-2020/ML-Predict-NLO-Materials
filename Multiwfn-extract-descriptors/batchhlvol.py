#!/usr/bin/python3 -u
import os, time

with open('homovol.sh', 'w') as oupt1 :
    oupt1.write('#!/bin/bash\n')
    oupt1.write('cat << EOF > $2-tmp-homovol.txt\n')
    oupt1.write('1000\n')
    oupt1.write('10\n')
    oupt1.write('16\n')
    oupt1.write('5\n')
    oupt1.write('4\n')
    oupt1.write('h\n')
    oupt1.write('3\n')
    oupt1.write('0\n')
    oupt1.write('13\n')
    oupt1.write('11\n')
    oupt1.write('13\n')
    oupt1.write('-1\n')
    oupt1.write('12\n')
    oupt1.write('1\n')
    oupt1.write('11\n')
    oupt1.write('0.05\n')
    oupt1.write('6\n')
    oupt1.write('EOF\n')
    oupt1.write('Multiwfn  $1 < $2-tmp-homovol.txt >> $2-homovol.txt\n')
    oupt1.write('rm ./$2-tmp-homovol.txt\n')
    oupt1.write('grep "Volume:" $2-homovol.txt|nl >> ${2}-homovol-result.txt\n')
    oupt1.write('grep "Estimated density according to mass and volume (M/V):" $2-homovol.txt|nl >> ${2}-homovol-result.txt\n')
    oupt1.write('grep "Overall surface area:" $2-homovol.txt|nl >> ${2}-homovol-result.txt\n')
    oupt1.write('rm ./$2-homovol.txt\n')

with open('lumovol.sh', 'w') as oupt2 :
    oupt2.write('#!/bin/bash\n')
    oupt2.write('cat << EOF > $2-tmp-lumovol.txt\n')
    oupt2.write('1000\n')
    oupt2.write('10\n')
    oupt2.write('16\n')
    oupt2.write('5\n')
    oupt2.write('4\n')
    oupt2.write('l\n')
    oupt2.write('3\n')
    oupt2.write('0\n')
    oupt2.write('13\n')
    oupt2.write('11\n')
    oupt2.write('13\n')
    oupt2.write('-1\n')
    oupt2.write('12\n')
    oupt2.write('1\n')
    oupt2.write('11\n')
    oupt2.write('0.05\n')
    oupt2.write('6\n')
    oupt2.write('EOF\n')
    oupt2.write('Multiwfn  $1 < $2-tmp-lumovol.txt >> $2-lumovol.txt\n')
    oupt2.write('rm ./$2-tmp-lumovol.txt\n')
    oupt2.write('grep "Volume:" $2-lumovol.txt|nl >> ${2}-lumovol-result.txt\n')
    oupt2.write('grep "Estimated density according to mass and volume (M/V):" $2-lumovol.txt|nl >> ${2}-lumovol-result.txt\n')
    oupt2.write('grep "Overall surface area:" $2-lumovol.txt|nl >> ${2}-lumovol-result.txt\n')
    oupt2.write('rm ./$2-lumovol.txt\n')

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
        #homo volume
        os.system('bash homovol.sh %s %s' %(sub_task, fns[0]))
        # To judge task if finishing    
        status_homo = False
        while not status_homo :
            if not os.path.exists(fns[0] + '-tmp-homovol.txt') :
                status_homo = True
            else : 
                time.sleep(3)
        #lumo volume
        os.system('bash lumovol.sh %s %s' %(sub_task, fns[0]))
        # To judge task if finishing    
        status_lumo = False
        while not status_lumo :
            if not os.path.exists(fns[0] + '-tmp-lumovol.txt') :
                status_lumo = True
            else : 
                time.sleep(3)
    #if os.path.exists('nohup.out') : os.system('rm nohup.out')          

