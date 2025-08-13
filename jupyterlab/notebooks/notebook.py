#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install huggingface_hub datasets


# In[3]:


get_ipython().system('huggingface-cli login --token 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')


# In[4]:


import os
from datasets import load_dataset


# In[8]:


dataset = load_dataset('csv', data_files={'train': "./../data/train.csv",'test': "./../data/test.csv",'sample_submission': "./../data/sample_submission.csv"})


# In[10]:


dataset.push_to_hub("aijk2")


# In[ ]:




