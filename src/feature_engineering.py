def create_features(df):
    df['day_of_month'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour
    user_venue_time = df.pivot_table(index='user', columns=['venue_type', 'day_of_month', 'hour'], aggfunc='size',
                                     fill_value=0)
    return user_venue_time


def apply_weights(timestamp, current_time):
    days_passed = (current_time - timestamp).days
    if days_passed < 7:
        return 5
    elif days_passed < 14:
        return 4
    elif days_passed < 21:
        return 3
    elif days_passed < 28:
        return 2
    else:
        return 1


def create_weighted_features(df):
    current_time = df['timestamp'].max()
    df['weight'] = df['timestamp'].apply(lambda x: apply_weights(x, current_time))
    user_venue_time_weighted = df.pivot_table(index='user', columns=['venue_type', 'day_of_month', 'hour'],
                                              values='weight', aggfunc='sum', fill_value=0)
    return user_venue_time_weighted
