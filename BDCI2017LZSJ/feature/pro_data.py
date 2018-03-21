
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:

def spliteData(df_proData):
    """
    对数据df_proData,分割成训练和测试数据集
    并给训练数据加上标签和测试数据分割开
    """
    df_label = pd.read_csv('../data/public/train.csv')

    df_train = df_proData[df_proData['EID'].isin(df_label['EID'])]
    df_test = df_proData[~df_proData['EID'].isin(df_label['EID'])]
    
    
    df_train = pd.merge(df_train,df_label[df_label['EID'].isin(df_train['EID'])],how ='left',on=['EID'])
    
    return df_train,df_test



