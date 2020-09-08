import numpy as np 
import matplotlib.pyplot as plt
import string
import os
import re
import sys
from scipy.optimize import curve_fit

exp_seq = sys.argv[1]
param = sys.argv[2]

if param == 'flex':
    paramcode = 2

if param == 'gravy':
    paramcode = 3

if param == 'iso':
    paramcode = 4

if param == 'arom':
    paramcode = 5

if param == 'ai':
    paramcode = 6

gens = []
paramvalues = []

if len(sys.argv) == 3:
    with open(exp_seq, 'r') as paramdata:
        l = 0
        for line in paramdata:
            l = l+1
            if l > 1:
                linestr = line.split()
                gens.append(int(linestr[1]))
                paramvalues.append(float(linestr[paramcode]))
    
    plt.scatter(gens,paramvalues,s=4)
    plt.xlabel('generations')
    plt.ylabel(param)
    plt.title(exp_seq.replace('_.txt','') + '\n' + param + ' vs. generation')
    plt.show()

if len(sys.argv) == 4:
    if sys.argv[3] == 'log':
        with open(exp_seq, 'r') as paramdata:
            l = 0
            for line in paramdata:
                l = l+1
                if l > 1:
                    linestr = line.split()
                    gens.append(int(linestr[1]))
                    paramvalues.append(float(linestr[paramcode]))
        
        def log(x,a,b,c):
            return a * np.log(b * np.asarray(x) + 1) + c
        
        popt, pcov = curve_fit(f=log, xdata=gens, ydata=paramvalues, bounds = (0,[max(paramvalues),1.,paramvalues[0]]))
        print('y = ' + str(popt[0]) + '*log(' + str(popt[1]) + 'x + 1) + ' + str(popt[2]))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(gens,paramvalues,s = 3,c = 'b',label = exp_seq.replace('_.txt',''))
        ax1.plot(gens,log(gens, *popt), 'r-',label = 'y = ' + str(round(popt[0],5)) + '*log(' + str(round(popt[1],5)) + 'x + 1) + ' + str(round(popt[2],5)))
        plt.title(exp_seq.replace('_.txt','') + '\n' + param + ' vs. generation')
        plt.xlabel('generations')
        plt.ylabel(param)
        plt.legend(loc ='lower right')
        plt.show()

    elif sys.argv[3] == '+exp':
        with open(exp_seq, 'r') as paramdata:
            l = 0
            for line in paramdata:
                l = l+1
                if l > 1:
                    linestr = line.split()
                    gens.append(int(linestr[1]))
                    paramvalues.append(float(linestr[paramcode]))
        
        def exponential(x,a,b,c):
            return a * np.exp(b * np.asarray(x)) + c
        
        popt, pcov = curve_fit(f=exponential, xdata=gens, ydata=paramvalues, bounds = (0,[max(paramvalues),1.,paramvalues[0]]))
        print('y = ' + str(popt[0]) + '*e^(' + str(popt[1]) + ') + ' + str(popt[2]))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(gens,paramvalues,s = 3,c = 'b',label = exp_seq.replace('_.txt',''))
        ax1.plot(gens,log(gens, *popt), 'r-',label = 'y = ' + str(round(popt[0],5)) + '*e^(' + str(round(popt[1],5)) + ') + ' + str(round(popt[2],5)))
        plt.title(exp_seq.replace('_.txt','') + '\n' + param + ' vs. generation')
        plt.xlabel('generations')
        plt.ylabel(param)
        plt.legend(loc ='lower right')
        plt.show()

    elif sys.argv[3] == '-exp':
        with open(exp_seq, 'r') as paramdata:
            l = 0
            for line in paramdata:
                l = l+1
                if l > 1:
                    linestr = line.split()
                    gens.append(int(linestr[1]))
                    paramvalues.append(float(linestr[paramcode]))
        
        def exponential(x,a,b,c):
            return a * np.exp(-b * np.asarray(x)) + c
        
        popt, pcov = curve_fit(f=exponential, xdata=gens, ydata=paramvalues, bounds = (0,[max(paramvalues),1.,paramvalues[0]]))
        print('y = ' + str(popt[0]) + '*e^(' + str(popt[1]) + ') + ' + str(popt[2]))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(gens,paramvalues,s = 3,c = 'b',label = exp_seq.replace('_.txt',''))
        ax1.plot(gens,log(gens, *popt), 'r-',label = 'y = ' + str(round(popt[0],5)) + '*e^(' + str(round(popt[1],5)) + ') + ' + str(round(popt[2],5)))
        plt.title(exp_seq.replace('_.txt','') + '\n' + param + ' vs. generation')
        plt.xlabel('generations')
        plt.ylabel(param)
        plt.legend(loc ='lower right')
        plt.show()

    else:
        exp_seq2 = sys.argv[2]
        param = sys.argv[3]
        gens2 = []
        paramvalues2 = []

        if param == 'flex':
            paramcode = 2

        if param == 'gravy':
            paramcode = 3

        if param == 'iso':
            paramcode = 4

        if param == 'arom':
            paramcode = 5

        if param == 'ai':
            paramcode = 6

        with open(exp_seq, 'r') as paramdata:
            l = 0
            for line in paramdata:
                l = l+1
                if l > 1:
                    linestr = line.split()
                    gens.append(int(linestr[1]))
                    paramvalues.append(float(linestr[paramcode]))
                    
        with open(exp_seq2, 'r') as paramdata2:
            l = 0
            for line in paramdata2:
                l = l+1
                if l > 1:
                    linestr = line.split()
                    gens2.append(int(linestr[1]))
                    paramvalues2.append(float(linestr[paramcode]))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(gens,paramvalues,s = 3,c = 'b',label = exp_seq.replace('_.txt',''))
        ax1.scatter(gens2,paramvalues2,s = 3,c = 'r',label = exp_seq2.replace('_.txt',''))
        plt.title(exp_seq.replace('_.txt','') + '\n'  + 'and' '\n' + exp_seq2.replace('_.txt','') + '\n' + param + ' vs. Generation')
        plt.legend(loc ='lower right')
        plt.show()


    






   


