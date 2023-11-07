import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(
    r"C:\Users\juanp\Desktop\boilerplate-medical-data-visualizer-main\boilerplate-medical-data-visualizer-main\medical_examination.csv"
)

# Task 1: Add an overweight column
df['overweight'] = (df['weight'] / (
    (df['height'] / 100)**2)).apply(lambda x: 1 if x > 25 else 0)

# Task 2: Normalize the data
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# Task 3: Convert the data into long format and create a catplot
"""
It combines the specified columns ('cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight') into a single column 'variable', and their corresponding values into a single column 'value'. The 'cardio' column is retained as an identifier. """

df_cat = pd.melt(df,
                 id_vars=['cardio'],
                 value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                     'overweight'
                 ])

print(df_cat)

# Create a catplot
fig = sns.catplot(data=df_cat,
                  x='variable',
                  hue='value',
                  col='cardio',
                  kind='count')

fig.savefig(
    r'C:\Users\juanp\Desktop\boilerplate-medical-data-visualizer-main\boilerplate-medical-data-visualizer-main\catplot.png'
)

# Task 4: Clean the data
df = df[(df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

# Task 5: Create a correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 8))

# Draw the heatmap with seaborn's heatmap()
sns.heatmap(corr,
            annot=True,
            fmt='.1f',
            mask=mask,
            vmax=.3,
            center=0,
            square=True,
            linewidths=.5,
            cbar_kws={"shrink": 0.5})

# Save figures
fig.savefig(
    r'C:\Users\juanp\Desktop\boilerplate-medical-data-visualizer-main\boilerplate-medical-data-visualizer-main\heatmap.png'
)
# Task 6: Draw a scatter plot matrix
df.drop(['cardio'], axis=1, inplace=True)
fig = sns.pairplot(df, hue='cardio')
fig.savefig(
    r'C:\Users\juanp\Desktop\boilerplate-medical-data-visualizer-main\boilerplate-medical-data-visualizer-main\scatterplot.png'
)
# Task 7: Draw a swarm plot matrix
fig = sns.pairplot(df, hue='cardio')
fig.savefig(
    r'C:\Users\juanp\Desktop\boilerplate-medical-data-visualizer-main\boilerplate-medical-data-visualizer-main\swarmplot.png'
)
