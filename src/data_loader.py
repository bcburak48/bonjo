import pandas as pd
from datetime import datetime
import json


def load_data(file_path):
    with open(file_path) as file:
        data = json.load(file)

    records = []
    for user, visits in data.items():
        for visit in visits:
            records.append({
                "user": user,
                "venue_type": visit["venue_type"],
                "timestamp": datetime.strptime(visit["ts"], "%Y-%m-%d %H:%M:%S.%f")
            })
    df = pd.DataFrame(records)
    return df
