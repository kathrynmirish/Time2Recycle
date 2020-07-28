#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:28:18 2020

@author: kmi20042005
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats 
import pandas as pd

#data formatted so no answer =0 green bin=1 black bin=2
before = pd.DataFrame.fillna(pd.read_csv('before.csv',usecols=[2,3,4,6,7,8,9,10,11,12]),value=0)
after = pd.DataFrame.fillna(pd.read_csv('after.csv',usecols=[2,3,4,6,7,8,9,10,11,12]),value=0)

#make list of column headings
header=list(before.columns)

#open a text file to store chisq results
file=open('chisqresults.txt','a')

#iterate to perform chi square test and make graph for each question
for i in range(0,len(header)):
    
    #counts instance of each answer 
    bobs=np.unique(before[header[i]],return_counts=True)[1][1:]
    aobs=np.unique(after[header[i]],return_counts=True)[1][1:]
    
    #find expected values for contingency table
    exp=stats.contingency.expected_freq([bobs,aobs])

    #perform and store chisq test 
    file.write("chi square results for "+header[i]+" p value is ")
    file.write(str(stats.chisquare(np.concatenate((bobs,aobs)),f_exp=np.concatenate(exp))[1]))
    file.write('                ')

    #general bar chart
    plt.bar(['green bin','black bin'],100*bobs/sum(bobs),width=0.35,align='edge',label='before')
    plt.bar(['green bin','black bin'],100*aobs/sum(aobs),width=-0.35,align='edge',label='after')
    plt.legend()
    plt.title("question regarding "+header[i])
    plt.savefig(header[i])
    plt.show()
    
file.close()