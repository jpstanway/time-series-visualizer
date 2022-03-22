import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date'] = df['date'].dt.strftime('%Y-%m')
df.rename(columns={'date': 'Date', 'value': 'Page Views'}, inplace=True)
df.set_index('Date', inplace=True)

# Clean data
df = df[df.isnull() == False]
df = df.loc[
    (df['Page Views'] >= df['Page Views'].quantile(0.025)) |
    (df['Page Views'] <= df['Page Views'].quantile(0.025))
]


def draw_line_plot():
    print(df)
    # Draw line plot
    fig = sns.lineplot(data=df, ci=None)
    fig.get_legend().remove()
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot

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

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
