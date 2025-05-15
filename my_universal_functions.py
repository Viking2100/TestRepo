#!/usr/bin/env python
# coding: utf-8

# In[5]:


def checkIfNotNumeric(*args):
    for x in args:
        if not (isinstance(x,(int,float))):
            return False
    return True

#checkIfNotNumeric(2,4.0, 12)


# In[6]:


def addAllNumerics(*args):
    s=0
    for x in args:
        s+=x
    return s


# In[ ]:


nyName = "Placeholder course name"

