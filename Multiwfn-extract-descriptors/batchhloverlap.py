#!/usr/bin/python3 -u
import os, time

with open('nhlmo.sh', 'w') as oupt1 :
    oupt1.write('#!/bin/bash\n')
    oupt1.write('cat << EOF > $2-tmp-hlomo.txt\n')
    oupt1.write('0\n')
    oupt1.write('1\n')
    oupt1.write('EOF\n')
    oupt1.write('Multiwfn  $1 < $2-tmp-hlomo.txt >> $2-hlomo.txt\n')
    oupt1.write('rm ./$2-tmp-hlomo.txt\n')
    oupt1.write('grep "Orbital" $2-hlomo.txt|nl | tail -n 2 >> ${2}-homo-lumo-number-result.txt\n')
    oupt1.write('rm ./$2-hlomo.txt\n')

with open('orboverlap.sh', 'w') as oupt2 :
    oupt2.write('#!/bin/bash\n')
    oupt2.write('cat << EOF > $2-tmp-orbital-overlap.txt\n')
    oupt2.write('1000\n')
    oupt2.write('10\n')
    oupt2.write('16\n')
    oupt2.write('100\n')
    oupt2.write('11\n')
    oupt2.write('$3,$4\n')
    oupt2.write('y\n')
    oupt2.write('EOF\n')
    oupt2.write('Multiwfn  $1 < $2-tmp-orbital-overlap.txt >> $2-orbital-overlap.txt\n')
    oupt2.write('rm ./$2-tmp-orbital-overlap.txt\n')
    oupt2.write('grep "Centroid distance between the two orbitals:" $2-orbital-overlap.txt | nl >> $2-orbital-overlap-result.txt\n')
    oupt2.write('grep "Overlap integral of norm of the two orbitals:" $2-orbital-overlap.txt | nl >> $2-orbital-overlap-result.txt\n')
    oupt2.write('rm ./$2-orbital-overlap.txt\n')

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
        os.system('bash nhlmo.sh %s %s' %(sub_task, fns[0]))
        # To judge task if finishing    
        status = False
        while not status :
            if not os.path.exists(fns[0] + '-tmp-hlomo.txt') :
                status= True
            else : 
                time.sleep(3)
        #number of HOMO and LUMO orbitals
        fn_hlnum =  fns[0] + '-homo-lumo-number-result.txt'
        hnum = os.popen('''grep 'HOMO' %s ''' %fn_hlnum).read().splitlines()[0].split()[3]
        lnum = os.popen('''grep 'LUMO' %s ''' %fn_hlnum).read().splitlines()[0].split()[2]
        os.system('bash orboverlap.sh %s %s %s %s' %(sub_task, fns[0], hnum, lnum))
        # To judge task if finishing    
        status = False
        while not status :
            if not os.path.exists(fns[0] + '-tmp-orbital-overlap.txt') :
                status= True
            else : 
                time.sleep(1)
    if os.path.exists('nohup.out') : os.system('rm nohup.out')          

