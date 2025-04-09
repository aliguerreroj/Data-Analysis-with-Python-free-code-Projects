

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv',index_col=0,parse_dates=True)

# Clean data
percentil_inferior = df['value'].quantile(0.025)
percentil_superior = df['value'].quantile(0.975)
df = df[(df['value'] >= percentil_inferior) & (df['value'] <= percentil_superior)]



def draw_line_plot():

    df_line = df.copy()

    plt.figure(figsize=(16, 6))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_line,color='red')

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
   
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()

    monthly_avg = df_bar.groupby(['Year', 'Month'])['value'].mean().reset_index()

    data_pivot = monthly_avg.pivot(index='Year', columns='Month', values='value')

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    data_pivot = data_pivot[month_order]

    colors = sns.color_palette("tab10", 12)

    plt.close('all') 
    fig, ax = plt.subplots(figsize=(12, 8))

    data_pivot.plot(kind='bar', ax=ax, color=colors)

    ax.set_title('Average Page Views per Month', fontsize=16)
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Average Page Views', fontsize=12)
    ax.legend(title='Months', fontsize=10)
    ax.grid(axis='y')

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = df_box['date'].dt.year
    df_box['Month'] = df_box['date'].dt.strftime('%b')

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(x='Year', y='value', hue='Year', data=df_box, ax=axes[0], palette='Set2', legend=False)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='Month', y='value', hue='Month', data=df_box, ax=axes[1], palette='Set3', order=month_order, legend=False)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()

    fig.savefig('box_plot.png')

    return fig


draw_line_plot()
draw_bar_plot()
draw_box_plot()