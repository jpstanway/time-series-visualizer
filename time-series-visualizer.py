import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
df.rename(columns={'value': 'page views'}, inplace=True)
df.set_index('date', inplace=True)

# Clean data
df = df[df.isnull() == False]
df = df.loc[
  (df['page views'] >= df['page views'].quantile(0.025)) &
  (df['page views'] <= df['page views'].quantile(0.975))
]

def sort_months(dfr):
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  dfr['month'] = pd.Categorical(dfr['month'], categories=months, ordered=True)
  dfr.sort_values('month', inplace=True)
  dfr.reset_index(inplace=True)
  return dfr;

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12,6))
    f = sns.lineplot(data=df, ci=None)
    f.get_legend().remove()
    f.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    f.set_xlabel('Date')
    f.set_ylabel('Page Views')
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]  
    df_bar['month'] = [d.strftime('%b') for d in df_bar.date]
    df_bar = sort_months(df_bar)
    df_bar.set_index('year', inplace=True)
    
    # Draw bar plot
    fig = plt.figure(figsize=(12,12))
    
    f = sns.barplot(data=df_bar, x=df_bar.index, y="page views", hue="month")
    f.legend(title="Months", labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], loc='upper left')
    f.set_xlabel('Years')
    f.set_ylabel('Average Page Views')
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(12,6), ncols=2, sharex=False)
    f1 = sns.boxplot(data=df_box, x='year', y='page views', ax=axes[0])
    f1.set_title('Year-wise Box Plot (Trend)')
    f1.set_xlabel('Year')
    f1.set_ylabel('Page Views')

    df_box = sort_months(df_box)
    
    f2 = sns.boxplot(data=df_box, x='month', y='page views', ax=axes[1])
    f2.set_title('Month-wise Box Plot (Seasonality)')
    f2.set_xlabel('Month')
    f2.set_ylabel('Page Views')
  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
