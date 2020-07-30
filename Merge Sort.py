#!/usr/bin/env python
# coding: utf-8

# In[347]:


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        leftlist = alist[:mid]
        rightlist = alist[mid:]
        
        mergeSort(leftlist)
        mergeSort(rightlist)
        
        i=0
        j=0
        k=0
        
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k]=leftlist[i]
                i=i+1
            else:
                alist[k]=rightlist[j]
                j=j+1
            k=k+1
            
        while i < len(leftlist):
            alist[k]=leftlist[i]
            i=i+1
            k=k+1

        while j < len(rightlist):
            alist[k]=rightlist[j]
            j=j+1
            k=k+1
    return alist


# In[348]:


alist = [6,2,4,1,3,7,5,8]
mergeSort(alist)
print(alist)


# In[ ]:




