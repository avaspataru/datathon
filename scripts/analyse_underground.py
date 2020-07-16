import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('london_underground_activity.csv')

years = [y for y in range(2007,2018)]
stations = set(df['station'].tolist())
print("Num of stations %d" % len(stations))

info = pd.read_csv('london_underground_station_info.csv')

# associate station with zone
station_to_zone = {}
for s in stations:
    r = info.loc[info['station'] == s]
    if r.empty:
        continue
    zone = r['zone'].values[0]

    station_to_zone[s] = zone

#only get zone 1 stations
stations_zone1 = []
for s in stations:
    if s in station_to_zone and station_to_zone[s] == '1':
        stations_zone1.append(s)
