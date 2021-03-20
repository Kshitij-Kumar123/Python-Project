import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where(df['weight'] / (df['height']/100)*(df['height']/100) > 25, 1, 0)

# Normalize data by making 0 always good and 1 always 
# bad. If the value of 'cholestorol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
print(df.columns)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` 
    # using just the values from 'cholesterol', 'gluc', 
    # 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    print(df_cat)
    # Group and reformat the data to split it by 'cardio'. 
    # Show the counts of each feature. 
    # You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    print(df_cat.head())
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable' , y= 'total', hue='value', col= 'cardio',  kind='bar', data = df_cat)

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df.loc[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df.loc[df['height'] <= df['height'].quantile(0.975)]
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df.loc[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df.loc[df['weight'] <= df['weight'].quantile(0.975)]


    print(df_heat.head())
    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson', min_periods=1)

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(7,7))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, cmap="YlGnBu", mask=mask, fmt='.1f', linewidths=.5, square=True, cbar_kws={'shrink':0.5}, annot=True, center=0)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

# draw_cat_plot()
draw_heat_map()