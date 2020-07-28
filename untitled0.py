#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:25:41 2020

@author: kmi20042005
"""

import matplotlib as plt
import pandas as pd

before = pd.read_csv(r'/home/kmi20042005/Projects/R/Time2Recycle/before.csv')
after = pd.read_csv(r'/home/kmi20042005/Projects/R/Time2Recycle/after.csv')

bmean=pd.DataFrame.mean(before)
print(bmean)