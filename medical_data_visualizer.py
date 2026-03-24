import pandas as pd
import matplotlib as plt
import seaborn as sb

#orvosi adatok megjelenítése

df = pd.read_csv('medical_examination.csv')

#bmi index kiszámítása, 
bmi = df['weight']/(df['height']*0.01)**2
#uj oszlop beszúrása, tulsúlyos - 1
df.loc[bmi>25,'overweight']=1
df.loc[bmi<=25,'overweight']=0

#adat normalizásás, 0 - jo
df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']>1,'cholesterol']=1
df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']>1,'gluc']=1
print(df.head())