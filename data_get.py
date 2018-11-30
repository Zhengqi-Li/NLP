#!/usr/bin/env python
# coding: utf-8

# In[200]:


import pandas as pd
train_data = pd.read_csv('train.csv')
train_data.head()


# In[199]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
import seaborn as sb
import matplotlib.pyplot as plt
stats = {}
labels = train_data.columns[2:].tolist()
for label in labels:
    stats.setdefault(label,train_data[train_data[label] == 1][label].count())
col_sum = train_data[labels].apply(lambda x: x.sum(), axis=1)
stats['clean'] = (col_sum == 0).sum()
x = list(stats.keys())
y = list(stats.values())
sb.set(rc={"figure.figsize": (8, 6)})
sb.barplot(x, y)
plt.title('# per class')
plt.xlabel('Type')
plt.ylabel('# of Occcurrences')
for a,b in enumerate(y):
    plt.text(a-0.25, b+0.05, s=b)


# In[201]:


tag_num = {}
for count in range(7):
    tag_num.setdefault(count, (col_sum == count).sum())
x = list(tag_num.keys())
y = list(tag_num.values())
sb.set(rc={"figure.figsize": (8, 6)})
sb.barplot(x, y, palette=sb.color_palette("Greens", 1))
plt.title('Multiple tags per comment')
plt.xlabel('# of tags')
plt.ylabel('# of Occcurrences')
for a,b in enumerate(y):
    plt.text(a-0.25, b+0.05, s=b)


# In[ ]:




