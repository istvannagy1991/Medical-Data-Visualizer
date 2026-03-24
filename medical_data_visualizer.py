import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def draw_cat_plot():
    #adatátalkitás long formátumba
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],  
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat.rename(columns={
        'variable': 'feature',
        'size': 'total'
    }, inplace=True)
    fig = sns.catplot(
        data=df_cat,
        x='feature',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # 1. Adattisztítás
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 2. Korrelációs mátrix
    corr = df_heat.corr()

    # 3. Maszk (felső háromszög eltüntetése)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 4. Figure létrehozása
    fig, ax = plt.subplots(figsize=(12, 10))

    # 5. Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    # DO NOT MODIFY THE NEXT TWO LINES
    fig.savefig('heatmap.png')
    return fig



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

    
