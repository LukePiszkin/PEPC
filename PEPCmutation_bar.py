
### Takes a PEPC .log file as input and consturts a bar chart of the distribution of amino acid residue substitutions ###

import numpy as np 
import string
import os
import re
import sys
import matplotlib.pyplot as plt

exp_seq = sys.argv[1]
log = []
muts = []

with open(exp_seq,'r') as mutdata:
    l = 0 
    for line in mutdata:
        l = l + 1
        log.append(line.split())      

for i in range(1,len(log)): 
    if log[i][7] == 'mutation:':
        muts.append([log[i][5],log[i][6]])
        

muts.sort()

hist = {}
for i in range(0,len(muts)):
    if muts[i-1] != muts[i]:
        hist.update({str(muts[i-1]) : i})

    hist.update({str(muts[-1]) : len(muts)})

sorted_hist = sorted(hist.items())

sorted_hist2 = [[sorted_hist[0][0], sorted_hist[0][1]]]

for i in range(1,len(sorted_hist)):
    sorted_hist2.append([sorted_hist[i][0], sorted_hist[i][1] - sorted_hist[i-1][1]])

sorted_hist2 = sorted(sorted_hist2,key = lambda x: x[1], reverse=True)

print(sorted_hist2)

objects = []
weights = []

for i in range(0,len(sorted_hist2)):
    objects.append(re.sub("'","",sorted_hist2[i][0])[1] + '\u2192' + re.sub("'","",sorted_hist2[i][0])[4])

for i in range(0,len(sorted_hist2)):
    weights.append(sorted_hist2[i][1])

y_pos = np.arange(len(objects))

if len(sys.argv) == 3:
    exp_seq2 = sys.argv[2]
    log2 = []
    muts2 = []

    with open(exp_seq2,'r') as mutdata2:
        l = 0 
        for line in mutdata2:
            l = l + 1
            log2.append(line.split())      

    for i in range(1,len(log2)): 
        if log2[i][7] == 'mutation:':
            muts2.append([log2[i][5],log2[i][6]])
            

    muts2.sort()

    hist2 = {}
    for i in range(0,len(muts2)):
        if muts2[i-1] != muts2[i]:
            hist2.update({str(muts2[i-1]) : i})

        hist2.update({str(muts2[-1]) : len(muts2)})

    sorted_hist2 = sorted(hist2.items())

    sorted_hist22 = [[sorted_hist2[0][0], sorted_hist2[0][1]]]

    for i in range(1,len(sorted_hist2)):
        sorted_hist22.append([sorted_hist2[i][0], sorted_hist2[i][1] - sorted_hist2[i-1][1]])

    sorted_hist22 = sorted(sorted_hist22,key = lambda x: x[1], reverse=True)

    print('\n')
    print(sorted_hist22)

    objects2 = []
    weights2 = []

    for i in range(0,len(sorted_hist22)):
        objects2.append(re.sub("'","",sorted_hist22[i][0])[1] + '\u2192' + re.sub("'","",sorted_hist22[i][0])[4])

    for i in range(0,len(sorted_hist22)):
        weights2.append(sorted_hist22[i][1])

    y_pos2 = np.arange(len(objects2))


fig, ax = plt.subplots()
width = 0.35

rects1 = ax.bar(y_pos - width/2,weights,width,label=exp_seq)
rects2 = ax.bar(y_pos2 + width/2,weights2,width,label=exp_seq2)

ax.set_xticks(y_pos)
ax.set_xticklabels(objects)
ax.set_ylabel('Number of Mutations')
ax.set_xlabel('Substitions')
ax.set_title(exp_seq + '\n' + exp_seq2 + '\n' + 'Mutations bar chart')

ax.legend()
plt.show()



