import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)

df['overweight'] = (df['BMI'] > 25).astype(int)


#3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

#     # 6
    df_cat = df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

#     # 7

    fig = sns.catplot(
        data=df_cat,
        kind='bar',
        x='variable',
        y='total',
        hue='value',
        col='cardio'
    )


#     # 8
    fig = draw_cat_plot()



#     # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = # Clean the df_heat DataFrame
df_heat = df_heat[
    (df_heat['ap_lo'] <= df_heat['ap_hi']) &  # diastolic <= systolic
    (df_heat['height'] >= df_heat['height'].quantile(0.025)) &  # height >= 2.5th percentile
    (df_heat['height'] <= df_heat['height'].quantile(0.975)) &  # height <= 97.5th percentile
    (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &  # weight >= 2.5th percentile
    (df_heat['weight'] <= df_heat['weight'].quantile(0.975))    # weight <= 97.5th percentile
]


    # 12
    corr = 

    # 13
    mask = 



#     # 14
#     fig, ax = None

#     # 15



# #     # 16
#     fig.savefig('heatmap.png')
#     return fig
