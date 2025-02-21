#!/usr/bin/env python
# coding: utf-8

# # First approach of Outliers Treatment through Boxplot (Interquartile Range)

# In[1]:


import pandas as pd

# In[2]:

my_df = pd.DataFrame({"input1" : [15,41,44,47,50,53,56,59,99],
                      "input2" : [29,41,44,47,50,53,56,59,66]})


# In[3]:


my_df.plot(kind="box",vert = False)


# In[5]:


outlier_columns =["input1", "input2"]


# In[6]:


for column in outlier_columns:
    lower_quartile = my_df[column].quantile(0.25)
    upper_quartile = my_df[column].quantile(0.75)
  
    iqr = upper_quartile - lower_quartile
    iqr_extended = iqr*1.5
    min_border = lower_quartile-iqr_extended
    max_border = upper_quartile+iqr_extended


# In[8]:


outliers = my_df[(my_df[column]<min_border)| (my_df[column]>max_border)].index 
print(f"{len(outliers)} outliers detected in column {column}")

#dropping the outliers from the column when it is found
my_df.drop(outliers,inplace=True)


# # Second Approach of Outlier Treatment through Mean and Standard Deviation

# In[9]:


my_df = pd.DataFrame({"input1" : [15,41,44,47,50,53,56,59,99],
                      "input2" : [29,41,44,47,50,53,56,59,66]})


# In[10]:


for column in outlier_columns:
    mean = my_df[column].mean()
    std_dev = my_df[column].std()
    min_border = mean-std_dev*3
    max_border = mean+std_dev*3
    


# In[11]:


outliers = my_df[(my_df[column]<min_border)| (my_df[column]>max_border)].index 
print(f"{len(outliers)} outliers detected in column {column}")

#dropping the outliers from the column when it is found
my_df.drop(outliers,inplace=True)


# In[ ]:




