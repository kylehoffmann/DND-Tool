#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv

with open('Magic10Normal5Items.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        
        print(' -  '.join(row))


# In[ ]:




