#!/usr/bin/env python
# coding: utf-8

# In[14]:


test_nums = [1721,979,366,299,675,1456]


# In[28]:


input_nums = []

# Get numbers to solve
try:
    f=open('input.txt',"r")
    for line in f:
        input_nums.append(int(line.strip('\n')))
    print(input_nums)
except:
    print("Failed to read file")


# In[24]:


import itertools

# Use numbers from file if exist or use test numbers
if not input_nums:
    combinations = itertools.combinations(test_nums, 2)
else:
    combinations = itertools.combinations(input_nums, 2)


for c in combinations:
    if c[0] + c[1] == 2020:
        print(c)
        print(c[0] * c[1])
        break


# In[ ]:



    

