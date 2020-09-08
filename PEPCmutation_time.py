import numpy as np 
import string
import os
import re
import sys
import matplotlib.pyplot as plt
import itertools
from operator import itemgetter

exp_seq = sys.argv[1]
log = []
muts = []
pos = []
objects = []
aminoperms = []
amino = []

with open(exp_seq,'r') as mutdata:
    l = 0 
    for line in mutdata:
        l = l + 1
        log.append(line.split()) 


for i in range(1,len(log)): 
    if log[i][7] == 'mutation:':
        muts.append([log[i][5],log[i][6]])
        pos.append(float(log[i][1]))

for i in range(0,len(muts)):
    objects.append(re.sub("'","",muts[i][0]) + '\u2192' + re.sub("'","",muts[i][1]))

plt.scatter(pos,objects)
plt.title(exp_seq + '\n' + 'Mutation Time Distribution')
plt.xlabel('Generation',fontsize = 12)
plt.ylabel('Substitution',fontsize = 12)
plt.show()
 
if len(sys.argv) == 3:  
    if sys.argv[2] == 'avg':
        mutspos = []
        for perm in itertools.permutations('ARNDBCEQZGHILKMFPSTWYV',2): # runs through permutations of resdidue subsitutions to check for matches
            if list(perm) in muts:
                for i in range(0,len(muts)):
                    if muts[i] == list(perm):
                        if muts[i] not in mutspos:
                            mutspos.append(muts[i])
                        mutspos.append(pos[i])
    

    objects2 = []
    mutsweightavg = []
    mutsweight = []
    mutsavg = []

    for i in range(0,len(mutspos)-1):
        if type(mutspos[i]) == list:
            n = 1
            

            while type(mutspos[i + n]) == float:
                n = n + 1

                if i + n == len(mutspos):
                    break
                
            # mutsweight.append([re.sub("'","",mutspos[i][0]) + '\u2192' + re.sub("'","",mutspos[i][1]), ])
            mutsweightavg.append([re.sub("'","",mutspos[i][0]) + '\u2192' + re.sub("'","",mutspos[i][1]), sum(mutspos[i+1:i+n])/len(mutspos[i+1:i+n]), n-1])


    mutsweightavg = sorted(mutsweightavg,key=itemgetter(2),reverse=True)

    for i in range(0,len(mutsweightavg)):
        objects2.append(mutsweightavg[i][0])
        mutsavg.append(mutsweightavg[i][1])
        mutsweight.append(10 * mutsweightavg[i][2])

fig, ax = plt.subplots()
ax.scatter(mutsavg[0:10],objects2[0:10],color = 'orange', label = 'Average', s = mutsweight[0:10])
ax.scatter(pos,objects,label = 'Substitution position')
ax.set_xlabel('Generation',fontsize = 12)
ax.set_ylabel('Substitution',fontsize = 12)
ax.set_ylim(top = 9.5)          
ax.legend(fontsize = 12, labelspacing = 1)
ax.set_title(exp_seq + '\n' + 'Top 10 Mutations Time Distribution with Average')
plt.show()

    
                        


