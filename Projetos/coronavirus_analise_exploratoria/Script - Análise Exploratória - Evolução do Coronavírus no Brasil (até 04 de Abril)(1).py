#!/usr/bin/env python
# coding: utf-8

# ### Análise Exploratória de Dados - Evolução do Coronavírus no Brasil até o dia 04 de Abril de 2020

# #### Victor Hugo Negrisoli - Desenvolvedor Full-Stack & Analista de Dados

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv('dataset/brazil_covid19.csv')


# In[8]:


df = df.rename(columns = {
    'date': 'data',
    'region': 'regiao',
    'state': 'estado',
    'cases': 'casos',
    'deaths': 'mortes'
})
df.tail(5)


# In[9]:


# Top 10 maiores estados agrupados por número de casos

analise_1 = df.groupby("estado").sum().sort_values(by = "casos").tail(10)


# In[10]:


analise_1.cumsum().plot(
    title = "Top 10 - Estados com maiores casos",
    figsize=(15, 5)
)


# In[11]:


# Função para converter valores do dataset no formato padrão

def converterData(data):
    dia = str(data[8:10])
    mes = str(data[5:7])
    ano = str(data[0:4])
    return '{}/{}/{}'.format(dia, mes, ano)


# In[12]:


datas = df["data"]
datas
for i in range(len(datas)):
    df.loc[i, "data"] = converterData(datas[i])


# In[13]:


analise_2 = df.groupby("data").sum().sort_values(by = "casos").tail(7)
analise_2.cumsum().plot(
    title = "Análise do crescimento de casos e mortes nos últimos 07 dias (04/04/2020)",
    figsize=(15, 5))

