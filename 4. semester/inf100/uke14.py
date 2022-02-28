import pandas as pd 
import datetime as dt

def read(file):
    data = pd.read_csv(file, sep=" ", names = ['year', 'month', 'day', 'hour', 'sealevel'])

    data['hour'] = data['hour'] - 1
    data['date'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
    data = data.set_index('date')
    
    return data.head

print(read("VIK_sealevel_2000.txt"))