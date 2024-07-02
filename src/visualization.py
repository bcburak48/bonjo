import matplotlib.pyplot as plt
import seaborn as sns


def plot_venue_visits(df):
    plt.figure(figsize=(14, 8))
    sns.countplot(data=df, x='venue_type', order=df['venue_type'].value_counts().index)
    plt.title('Number of Visits to Each Type of Venue')
    plt.xlabel('Venue Type')
    plt.ylabel('Number of Visits')
    plt.xticks(rotation=45)
    plt.show()


def plot_visits_over_time(df):
    plt.figure(figsize=(14, 8))
    df['timestamp'].dt.date.value_counts().sort_index().plot()
    plt.title('Number of Visits Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Visits')
    plt.xticks(rotation=45)
    plt.show()
