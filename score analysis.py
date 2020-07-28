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

bcount=np.unique(before,return_counts=True)
acount=np.unique(after,return_counts=True)

bperc=bcount[1]*100/len(before)
aperc=acount[1]*100/len(after)

file=open('ttestresults.txt','a')

file.write('t test p value is')
file.write(str(stats.ttest_ind(before,after)[1]))
file.close()

plt.bar(bcount[0],bperc,color='b',width=0.35,align='edge',label='before')
plt.bar(acount[0],aperc,color='g',width=-0.35,align='edge',label='after')
plt.xticks(np.arange(16))
plt.ylabel('percentage of cohort')
plt.title('quiz scores before and after time 2 recycle')
plt.legend()
plt.savefig('quizscores')
plt.show()