#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np


# In[2]:


#Ideen
#Tabelle mit allen Vereinen machen mit einzelnen Attributen
#z.B. durchschnittliche (Heim-/Auswärts-)Tore, Häufigkeit Über-/Untertore usw.
#Zahlen bereinigen je nachdem, wie lange es her ist.
#Heim-/Auswärtsstärke über Siege, Unentschieden und Niederlagen definieren


# In[11]:


#Daten einfügen
BL=pd.concat([pd.read_csv("Daten/Bundesliga/BL1112.csv"),pd.read_csv("Daten/Bundesliga/BL1213.csv"),pd.read_csv("Daten/Bundesliga/BL1314.csv"),pd.read_csv("Daten/Bundesliga/BL1415.csv"),pd.read_csv("Daten/Bundesliga/BL1516.csv"),pd.read_csv("Daten/Bundesliga/BL1617.csv"),pd.read_csv("Daten/Bundesliga/BL1718.csv"),pd.read_csv("Daten/Bundesliga/BL1819.csv"),pd.read_csv("Daten/Bundesliga/BL1920.csv"),pd.read_csv("Daten/Bundesliga/BL2021.csv"),pd.read_csv("Daten/Bundesliga/BL2122.csv")])
PL=pd.concat([pd.read_csv("Daten/Premier League/PL1112.csv"),pd.read_csv("Daten/Premier League/PL1213.csv"),pd.read_csv("Daten/Premier League/PL1314.csv"),pd.read_csv("Daten/Premier League/PL1415.csv"),pd.read_csv("Daten/Premier League/PL1516.csv"),pd.read_csv("Daten/Premier League/PL1617.csv"),pd.read_csv("Daten/Premier League/PL1718.csv"),pd.read_csv("Daten/Premier League/PL1819.csv"),pd.read_csv("Daten/Premier League/PL1920.csv"),pd.read_csv("Daten/Premier League/PL2021.csv"),pd.read_csv("Daten/Premier League/PL2122.csv")])
SA=pd.concat([pd.read_csv("Daten/Serie A/S1112.csv"),pd.read_csv("Daten/Serie A/S1213.csv"),pd.read_csv("Daten/Serie A/S1314.csv"),pd.read_csv("Daten/Serie A/S1415.csv"),pd.read_csv("Daten/Serie A/S1516.csv"),pd.read_csv("Daten/Serie A/S1617.csv"),pd.read_csv("Daten/Serie A/S1718.csv"),pd.read_csv("Daten/Serie A/S1819.csv"),pd.read_csv("Daten/Serie A/S1920.csv"),pd.read_csv("Daten/Serie A/S2021.csv"),pd.read_csv("Daten/Serie A/S2122.csv")])
SP=pd.concat([pd.read_csv("Daten/La Liga/SP1112.csv"),pd.read_csv("Daten/La Liga/SP1213.csv"),pd.read_csv("Daten/La Liga/SP1314.csv"),pd.read_csv("Daten/La Liga/SP1415.csv"),pd.read_csv("Daten/La Liga/SP1516.csv"),pd.read_csv("Daten/La Liga/SP1617.csv"),pd.read_csv("Daten/La Liga/SP1718.csv"),pd.read_csv("Daten/La Liga/SP1819.csv"),pd.read_csv("Daten/La Liga/SP1920.csv"),pd.read_csv("Daten/La Liga/SP2021.csv"),pd.read_csv("Daten/La Liga/SP2122.csv")])


# In[12]:


SA.dropna(axis=0,subset={"FTHG","FTAG"},inplace=True)
PL.dropna(axis=0,subset={"FTHG","FTAG"},inplace=True)
BL.dropna(axis=0,subset={"FTHG","FTAG"},inplace=True)
SP.dropna(axis=0,subset={"FTHG","FTAG"},inplace=True)


# In[13]:


SA["FTHG"]=SA["FTHG"].astype(int)
SA["FTAG"]=SA["FTAG"].astype(int)
SP["FTHG"]=SP["FTHG"].astype(int)
SP["FTAG"]=SP["FTAG"].astype(int)
PL["FTHG"]=PL["FTHG"].astype(int)
PL["FTAG"]=PL["FTAG"].astype(int)
BL["FTHG"]=BL["FTHG"].astype(int)
BL["FTAG"]=BL["FTAG"].astype(int)


# In[14]:


BL["Ergebnis"]=BL["FTHG"].astype(str)+"-"+BL["FTAG"].astype(str)
PL["Ergebnis"]=PL["FTHG"].astype(str)+"-"+PL["FTAG"].astype(str)
SA["Ergebnis"]=SA["FTHG"].astype(str)+"-"+SA["FTAG"].astype(str)
SP["Ergebnis"]=SP["FTHG"].astype(str)+"-"+SP["FTAG"].astype(str)


# In[15]:


BL["Differenz"]=BL["FTHG"]-BL["FTAG"]
PL["Differenz"]=PL["FTHG"]-PL["FTAG"]
SA["Differenz"]=SA["FTHG"]-SA["FTAG"]
SP["Differenz"]=SP["FTHG"]-SP["FTAG"]


# In[16]:


BL["Tore"]=BL["FTHG"]+BL["FTAG"]
PL["Tore"]=PL["FTHG"]+PL["FTAG"]
SA["Tore"]=SA["FTHG"]+SA["FTAG"]
SP["Tore"]=SP["FTHG"]+SP["FTAG"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[74]:


#Häufigkeit, wie oft ein Spiel dieses Teams mit über 2,5 Toren ausgegangen ist
x={}
liste=[]
for team in BL["HomeTeam"].unique():
    Mannschaft=team
    Prozent=round(len(BL.loc[((BL["HomeTeam"]==team)|(BL["AwayTeam"]==team))&(BL["Tore"]>2.5)])/len(BL.loc[((BL["HomeTeam"]==team)|(BL["AwayTeam"]==team))]),2)
    x[Mannschaft]=x.get(Mannschaft,Prozent)
    
for key, value in x.items():
    liste.append((value,key))
    
print(sorted(liste,reverse=True))


# In[105]:


x={}
liste=[]
for team in PL["HomeTeam"].unique():
    Mannschaft=team
    Prozent=round(len(PL.loc[((PL["HomeTeam"]==team)|(PL["AwayTeam"]==team))&(PL["Tore"]>2.5)])/len(PL.loc[((PL["HomeTeam"]==team)|(PL["AwayTeam"]==team))]),2)
    x[Mannschaft]=x.get(Mannschaft,Prozent)
    
for key, value in x.items():
    liste.append((value,key))
    
print(sorted(liste,reverse=True))


# In[115]:


x={}
liste=[]
for team in SA["HomeTeam"].unique():
    Mannschaft=team
    Prozent=round(len(SA.loc[((SA["HomeTeam"]==team)|(SA["AwayTeam"]==team))&(SA["Tore"]>2.5)])/len(SA.loc[((SA["HomeTeam"]==team)|(SA["AwayTeam"]==team))]),2)
    x[Mannschaft]=x.get(Mannschaft,Prozent)
    
for key, value in x.items():
    liste.append((value,key))
    
print(sorted(liste,reverse=True))


# In[114]:


x={}
liste=[]
for team in SP["HomeTeam"].unique():
    Mannschaft=team
    Prozent=round(len(SP.loc[((SP["HomeTeam"]==team)|(SP["AwayTeam"]==team))&(SP["Tore"]>2.5)])/len(SP.loc[((SP["HomeTeam"]==team)|(SP["AwayTeam"]==team))]),2)
    x[Mannschaft]=x.get(Mannschaft,Prozent)
    
for key, value in x.items():
    liste.append((value,key))
    
print(sorted(liste,reverse=True))


# In[ ]:





# In[ ]:





# In[ ]:





# In[150]:


#Durchschnittliche Anzahl an Toren [Team: Gesamt, Heim, Auswärts]
Gesamt={}
liste=[]
for team in BL["HomeTeam"].unique():
    Mannschaft=team
    dtore=round((BL.loc[(BL["HomeTeam"]==team)]["FTHG"].sum()+BL.loc[(BL["AwayTeam"]==team)]["FTAG"].sum())/len(BL.loc[(BL["HomeTeam"]==team) | (BL["AwayTeam"]==team)]),2)
    dhtore=round(BL.loc[(BL["HomeTeam"]==team)]["FTHG"].sum()/len(BL.loc[BL["HomeTeam"]==team]),2)
    datore=round(BL.loc[(BL["AwayTeam"]==team)]["FTAG"].sum()/len(BL.loc[BL["AwayTeam"]==team]),2)
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dtore,dhtore,datore])
Gesamt


# In[154]:


Gesamt={}
liste=[]
for team in PL["HomeTeam"].unique():
    Mannschaft=team
    dtore=round((PL.loc[(PL["HomeTeam"]==team)]["FTHG"].sum()+PL.loc[(PL["AwayTeam"]==team)]["FTAG"].sum())/len(PL.loc[(PL["HomeTeam"]==team) | (PL["AwayTeam"]==team)]),2)
    dhtore=round(PL.loc[(PL["HomeTeam"]==team)]["FTHG"].sum()/len(PL.loc[PL["HomeTeam"]==team]),2)
    datore=round(PL.loc[(PL["AwayTeam"]==team)]["FTAG"].sum()/len(PL.loc[PL["AwayTeam"]==team]),2)
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dtore,dhtore,datore])
Gesamt


# In[155]:


Gesamt={}
liste=[]
for team in SA["HomeTeam"].unique():
    Mannschaft=team
    dtore=round((SA.loc[(SA["HomeTeam"]==team)]["FTHG"].sum()+SA.loc[(SA["AwayTeam"]==team)]["FTAG"].sum())/len(SA.loc[(SA["HomeTeam"]==team) | (SA["AwayTeam"]==team)]),2)
    dhtore=round(SA.loc[(SA["HomeTeam"]==team)]["FTHG"].sum()/len(SA.loc[SA["HomeTeam"]==team]),2)
    datore=round(SA.loc[(SA["AwayTeam"]==team)]["FTAG"].sum()/len(PL.loc[SA["AwayTeam"]==team]),2)
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dtore,dhtore,datore])
Gesamt


# In[156]:


Gesamt={}
liste=[]
for team in SP["HomeTeam"].unique():
    Mannschaft=team
    dtore=round((SP.loc[(SP["HomeTeam"]==team)]["FTHG"].sum()+SP.loc[(SP["AwayTeam"]==team)]["FTAG"].sum())/len(SP.loc[(SP["HomeTeam"]==team) | (SP["AwayTeam"]==team)]),2)
    dhtore=round(SP.loc[(SP["HomeTeam"]==team)]["FTHG"].sum()/len(SP.loc[SP["HomeTeam"]==team]),2)
    datore=round(SP.loc[(SP["AwayTeam"]==team)]["FTAG"].sum()/len(SP.loc[SP["AwayTeam"]==team]),2)
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dtore,dhtore,datore])
Gesamt


# In[ ]:





# In[ ]:





# In[53]:


#Durchschnittliche Tore letzte 5 Heim-/Auswärtsspiele (Heimtore, Heimgegentore, Auswärtstore, Auswärtsgegentore)
Gesamt={}
liste=[]
for team in BL["HomeTeam"].unique():
    Mannschaft=team
    dhtore=BL.loc[(BL["HomeTeam"]==team)].tail(5).FTHG.sum()/5
    dhgtore=BL.loc[(BL["HomeTeam"]==team)].tail(5).FTAG.sum()/5
    datore=BL.loc[(BL["AwayTeam"]==team)].tail(5).FTAG.sum()/5
    dagtore=BL.loc[(BL["AwayTeam"]==team)].tail(5).FTHG.sum()/5
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dhtore, dhgtore, datore, dagtore])
Gesamt


# In[54]:


Gesamt={}
liste=[]
for team in PL["HomeTeam"].unique():
    Mannschaft=team
    dhtore=PL.loc[(PL["HomeTeam"]==team)].tail(5).FTHG.sum()/5
    dhgtore=PL.loc[(PL["HomeTeam"]==team)].tail(5).FTAG.sum()/5
    datore=PL.loc[(PL["AwayTeam"]==team)].tail(5).FTAG.sum()/5
    dagtore=PL.loc[(PL["AwayTeam"]==team)].tail(5).FTHG.sum()/5
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dhtore, dhgtore, datore, dagtore])
Gesamt


# In[56]:


Gesamt={}
liste=[]
for team in SP["HomeTeam"].unique():
    Mannschaft=team
    dhtore=SP.loc[(SP["HomeTeam"]==team)].tail(5).FTHG.sum()/5
    dhgtore=SP.loc[(SP["HomeTeam"]==team)].tail(5).FTAG.sum()/5
    datore=SP.loc[(SP["AwayTeam"]==team)].tail(5).FTAG.sum()/5
    dagtore=SP.loc[(SP["AwayTeam"]==team)].tail(5).FTHG.sum()/5
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dhtore, dhgtore, datore, dagtore])
Gesamt


# In[57]:


Gesamt={}
liste=[]
for team in SA["HomeTeam"].unique():
    Mannschaft=team
    dhtore=SA.loc[(SA["HomeTeam"]==team)].tail(5).FTHG.sum()/5
    dhgtore=SA.loc[(SA["HomeTeam"]==team)].tail(5).FTAG.sum()/5
    datore=SA.loc[(SA["AwayTeam"]==team)].tail(5).FTAG.sum()/5
    dagtore=SA.loc[(SA["AwayTeam"]==team)].tail(5).FTHG.sum()/5
    Gesamt[Mannschaft]=Gesamt.get(Mannschaft,[dhtore, dhgtore, datore, dagtore])
Gesamt


# In[ ]:


#'Dortmund': [Gesamt: 2.22, Heim: 2.52, Auswärts: 1.93]


# In[33]:


#Durchschnittliche Tore letzte 5 Heimspiele
Bundesliga.loc[(Bundesliga["HomeTeam"]=="Dortmund")].tail(5).FTHG.sum()/5


# In[43]:


#Durchschnittliche Gegentore letzte 5 Heimspiele
Bundesliga.loc[(Bundesliga["HomeTeam"]=="Dortmund")].tail(5).FTAG.sum()/5


# In[42]:


#Durchschnittliche Tore letzte 5 Auswärtsspiele
Bundesliga.loc[(Bundesliga["AwayTeam"]=="Dortmund")].tail(5).FTAG.sum()/5


# In[46]:


#Durchschnittliche Gegentore letzte 5 Auswärtsspiele
Bundesliga.loc[(Bundesliga["AwayTeam"]=="Dortmund")].tail(5).FTHG.sum()/5


# In[25]:


Bundesliga=BL[["HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "Ergebnis", "Differenz", "Tore"]]


# In[52]:


Bundesliga.loc[(Bundesliga["HomeTeam"]=="Bayern Munich")].tail(5)

