def classify_user(user_data):
    day_visits = user_data[user_data['hour'].between(6, 18)].shape[0]
    night_visits = user_data[user_data['hour'].between(19, 5)].shape[0]
    weekday_visits = user_data[user_data['timestamp'].dt.weekday < 5].shape[0]
    weekend_visits = user_data[user_data['timestamp'].dt.weekday >= 5].shape[0]

    sun_moon_lover = 'Güneş sever' if day_visits >= night_visits else 'Ay sever'
    week_weekend_lover = 'Haftasonu sever' if weekend_visits >= weekday_visits else 'Hafta içi sever'

    venue_visits = user_data['venue_type'].value_counts()
    venue_lover = venue_visits.idxmax() + ' sever'

    return sun_moon_lover, week_weekend_lover, venue_lover


def classify_users(df):
    import pandas as pd
    classifications = []
    for user, user_data in df.groupby('user'):
        classifications.append([user] + list(classify_user(user_data)))
    user_classifications = pd.DataFrame(classifications,
                                        columns=['user', 'Zaman Tercihi', 'Hafta Tercihi', 'Mekan Tercihi'])
    return user_classifications
