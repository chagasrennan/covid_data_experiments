import pandas as pd

def get_full_DataSet():
    return pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=['date'])

def get_country(df, cols, code):
    return df[(df.iso_code.isin(code))][cols].copy()