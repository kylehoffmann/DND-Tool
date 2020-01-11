#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
import sys

readFileName = '../Resources/Magic10Normal5Items.csv'
if len(sys.argv) > 1:
	readFileName = sys.argv[1]

with open(readFileName, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
    	#pass      
        print(' -  '.join(row))

#print("Hello World")




