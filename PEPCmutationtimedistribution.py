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