import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set

file_path = "C:/Users/rtran/OneDrive/Desktop/Py(VS)/daily/FIFA/data.csv"
records = pd.read_csv(file_path)
records.head()

def country(x):
    return records[records['Nationality']==x][['Name','Overall','Age','Potential','Club']]

country('Brazil')

def club(x):
    return records[records['Club']==x][['Name','Overall','Age','Potential','Wage','Contract Valid Until','Release Clause']]

club('FC Barcelona')

plt.figure(figsize = (18, 8))
plt.style.use('fivethirtyeight')
ax = sns.countplot(x='Position', data=records, palette='coolwarm')
ax.set_xlabel(xlabel='Different Positions in Football', fontsize=16)
ax.set_ylabel(ylabel='Count of Players', fontsize=16)

plt.show()

sns.lmplot(x = 'SprintSpeed', y = 'Agility', data = records, col = 'Preferred Foot')
plt.show()

x = records.Overall
plt.figure(figsize=(12,8))
plt.style.use('seaborn-dark')

ax = sns.distplot(x, bins = 58, kde = False, color = 'y')
ax.set_xlabel(xlabel = "Players Overall", fontsize = 16)
ax.set_ylabel(ylabel = 'Number of players', fontsize = 16)
ax.set_title(label = 'Histogram of players ovr', fontsize = 20)
plt.show()