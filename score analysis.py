#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:25:41 2020

@author: kmi20042005
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats 

#importing list of scores as array
after = np.genfromtxt('after.csv',delimiter=',',usecols=(16))
before = np.genfromtxt('before.csv',delimiter=',',usecols=(16))

#open file for summary data 
file2=open('summaryscores.txt','a')

#storing summary data
file2.write('summary data for after ')
file2.write(str(stats.describe(after)))
file2.write('             summary data for before ')
file2.write(str(stats.describe(before)))
file2.close()

#open file to store results of t test 
file=open('ttestresults.txt','a')

#perform 2 sample t test
file.write('t test p value is')
file.write(str(stats.ttest_ind(before,after)[1]))
file.close()

#count data for scores
bcount=np.unique(before,return_counts=True)
acount=np.unique(after,return_counts=True)

#converting count data to % of cohort as n1!=n2
bperc=bcount[1]*100/len(before)
aperc=acount[1]*100/len(after)

#plotting bar chart of count data
plt.bar(bcount[0],bperc,color='b',width=0.35,align='edge',label='before')
plt.bar(acount[0],aperc,color='g',width=-0.35,align='edge',label='after')
plt.xticks(np.arange(16))
plt.ylabel('percentage of cohort')
plt.title('quiz scores before and after time 2 recycle')
plt.legend()
plt.savefig('quizscores')
plt.show()

