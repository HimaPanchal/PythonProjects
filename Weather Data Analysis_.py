#!/usr/bin/env python
# coding: utf-8

# ## How to Analyze Weather Data Using Python: A Step-by-Step Guide
# 

# Analyzing weather data is a fascinating exercise in understanding the relationship between different environmental variables. Below, I'll walk you through a Python script that processes and visualizes a weather dataset.
# 
# 

# In[40]:


#Importing popular libraries
import pandas as pd # Pandas for data manupulation
import numpy as np # Numpy for numerical operations
import matplotlib.pyplot as plt #Matplotlib and Seaborn for visualizations
import seaborn as sns
from importlib import reload
plt = reload(plt) # reloading plt ensures a clean slate for our visualizations.


# # Load and Inspect Data

# In[41]:


df = pd.read_csv(r'./weatherHistory.csv')


# In[42]:


df.head() # previewing the first five rows to understand its structure


# # Data Overview 

# In[43]:


df.info() # This shows the number of non-null entries per column and data types


# In[44]:


df.describe() # This provides statistical insights(mean, median etc) for numerical columns


# In[45]:


df['Precip Type'].value_counts()


# # Handling Missing Values

# In[46]:


df['Precip Type'].fillna("rain", inplace = True)


# In[47]:


df.isnull().sum()


# # Drop Irrelevant Columns

# In[48]:


df.drop(["Daily Summary"], axis = 1, inplace=True) # Daily Summary column is removed as it's not needed for this analysis.


# In[49]:


df.columns


# # Split and Clean Date Column

# In[50]:


df[["Date-Time", "TZ"]] = df["Formatted Date"].str.split("+", expand=True) #Date-Time is converted to a datetime object for easier manipulation.
df["Date-Time"] = pd.to_datetime(df["Date-Time"]) #The FormattedDate column is split into Date-Time and TZ (timezone).
df.head()


# In[51]:


columns_order=["Date-Time","TZ","Summary","Precip Type","Temperature (C)","Apparent Temperature (C)",
                "Humidity","Wind Speed (km/h)","Wind Bearing (degrees)","Visibility (km)","Loud Cover",
                "Pressure (millibars)", "Daily Summary"]
df=df.reindex(columns=columns_order)
df=df.drop(columns="TZ")
df.head()


# In[52]:


df["Date-Time"]=pd.to_datetime(df["Date-Time"])
df.info()


# # Feature Engineering

# In[53]:


df["Year"]=pd.DatetimeIndex(df["Date-Time"]).year
df["Month"]=df["Date-Time"].dt.month_name()
df["day"]=df["Date-Time"].dt.day
df.head()


# In[54]:


df["Wind Speed (km/h)"].describe()


# In[55]:


avg_wind_Speed=pd.DataFrame(df.groupby("Year")["Wind Speed (km/h)"].mean())
avg_wind_Speed
#=["Year","AVG. Wind Speed (km/hr"]


# In[56]:


fig,ax=plt.subplots(figsize=(10,8))
sns.lineplot(x=avg_wind_Speed.index,y=avg_wind_Speed["Wind Speed (km/h)"])
plt.title("Average wind speed over the yeears")


# In[57]:


month_avg_wind_Speed=pd.DataFrame(df.groupby("Month")["Wind Speed (km/h)"].mean())
order=["January","February","March","April","May","June","July","August","September",
            "October","November","December"]
monthly_wind_speed=month_avg_wind_Speed.reindex(index=order)
monthly_wind_speed


# In[58]:


fig,ax=plt.subplots(figsize=(10,8))
sns.lineplot(x=monthly_wind_speed.index,y=monthly_wind_speed["Wind Speed (km/h)"])
plt.title("Monthly Average wind speed over the yeears")


# In[59]:


df["Summary"].value_counts()


# In[60]:


weather_cond=pd.DataFrame(df.groupby("Year")["Summary"].describe(include="O").top)

weather_cond.rename(columns={"top":"most frequent weather"})


# In[61]:


m_weather_cond=pd.DataFrame(df.groupby("Month")["Summary"].describe(include="O").top)
order=["January","February","March","April","May","June","July","August","September",
            "October","November","December"]
m_weather_cond.rename(columns={"top":"most frequent weather"})
monthly=m_weather_cond.reindex(index=order)
monthly


# In[62]:


month_avg_visibility=pd.DataFrame(df.groupby("Month")["Visibility (km)"].mean())
order=["January","February","March","April","May","June","July","August","September",
            "October","November","December"]
monthly_visibility=month_avg_visibility.reindex(index=order)
monthly_visibility


# In[63]:


fig,ax=plt.subplots(figsize=(10,8))
sns.lineplot(x=monthly_visibility.index,y=monthly_visibility["Visibility (km)"])
plt.title("Monthly visibility over the yeears")


# In[65]:


percip=pd.DataFrame(df.groupby("Month")["Precip Type"].describe(include="O").top)
order=["January","February","March","April","May","June","July","August","September",
            "October","November","December"]
m_p=percip.rename(columns={"top":"Precip Type"})
monthly_percip=m_p.reindex(index=order)
monthly_percip


# In[74]:


fig,ax=plt.subplots(figsize=(10,8))
plt.hist(df["Temperature (C)"],bins=10,rwidth=0.9)
plt.xlabel("Temperature (C)")
plt.ylabel("frequency")


# In[68]:


year_avg_temp=pd.DataFrame(df.groupby("Year")["Temperature (C)"].mean())
year_avg_temp


# In[69]:


fig,ax=plt.subplots(figsize=(10,8))
sns.lineplot(x=year_avg_temp.index,y=year_avg_temp["Temperature (C)"])
plt.title("Annual avg. temperature")


# In[70]:


month_temp=pd.DataFrame(df.groupby("Month")["Temperature (C)"].mean())
order=["January","February","March","April","May","June","July","August","September",
            "October","November","December"]

monthly_avg_temp=month_temp.reindex(index=order)
monthly_avg_temp


# In[71]:


fig,ax=plt.subplots(figsize=(10,8))
sns.lineplot(x=monthly_avg_temp.index,y=monthly_avg_temp["Temperature (C)"])
plt.title("monthly avg. temperature")


# In[72]:


df4=df.drop(columns=["Year","day","Loud Cover"])
d_corr=df4.corr()
d_corr


# In[73]:


fig,ax=plt.subplots(figsize=(10,8))
sns.heatmap(d_corr,annot=True,cmap='magma_r',linewidths=0.2)
plt.title("correlations heat map")


# In[ ]:





# In[ ]:




