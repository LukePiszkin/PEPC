import numpy as np 
import matplotlib.pyplot as plt
import string
import os
import re
import sys

exp_seq = sys.argv[1]

gens = []

with open(exp_seq, 'r') as paramdata:
        l = 0
        for line in paramdata:
            l = l+1
            if l > 1:
                linestr = line.split()
                gens.append(int(linestr[1]))

P = len(gens) - 1

print('\n')
print('Number of suscessful mutations = ' + str(P))

logfile = exp_seq.strip('.txt') + '.log'

with open(logfile, 'r') as file:
    for last_line in file:
        pass

print('Average number of successful mutations = ' + str(float(P)/float(last_line.split()[1])))

def gensdelta(mutations):
    deltas = []
    for i in range(1,len(mutations)):
        deltas.append(mutations[i] - mutations[i-1])
    print('Mean distance between mutations = ' + str(np.average(deltas)))
    print('Variance = ' + str(np.var(deltas)))
    print('Index of dispersion (Variance/Mean) = ' + str(np.var(deltas)/np.average(deltas)))
    plt.scatter(mutations[:-1],deltas)
    plt.xlabel('Generation')
    plt.ylabel('Distance Between Mutations (' + '\u0394' + ')')
    plt.title(exp_seq + '\n' + 'Distance Between Mutations (' + '\u0394' + ') vs. Generation')
    plt.show()

gensdelta(gens)

