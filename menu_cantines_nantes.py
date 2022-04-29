#!/usr/bin/env python
# coding: utf-8

# Analyse des menus des cantines de Nantes pour évaluer l'augmentation des repas végétariens et le respect de la réglementation

# In[1]:


#importation des librairies pour l'analyse
import pandas as pd
import regex as re


# In[17]:


# Importation du fichier issu du site https://data.nantesmetropole.fr/pages/home/
# Le fichier correspond à une projection des menus dans les 2 mois à venir, il s'agit d'une prédiction
df = pd.read_csv('244400404_menus-cantines-scolaires-nantes.csv',sep=';',low_memory=True)
# le fichier ne comporte que 69 ligne, il est mis à jour toutes les semaines. 
# il faut ajouter régulièrement les mises à jour


# In[18]:


df.describe()


# In[22]:


df.info()


# In[34]:


df.head(10)


# In[33]:


df['week']=df['Date'].dt.isocalendar().week


# In[ ]:


# Transformer la colonne date en type date
df['Date']= pd.to_datetime(df['Date'])
# Je créé une colonne mois à partir de la date
df['mois']=df['Date'].dt.month
# Je créé une colonne année à partir de la date
df['annee']=df['Date'].dt.year
df['doy']=df['Date'].dt.dayofyear
df['dow']=df['Date'].dt.dayofweek

# Créer une colonne qui indique le numéro de la semaine en fonction de la date du jour
df['week']=df['Date'].dt.isocalendar().week

# extraire du repas dans une colonne à part le motif "Menu végétarien"

