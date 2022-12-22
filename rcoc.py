import pandas as pd
import random

data = pd.read_csv('./cities.csv')

def get_random_city():
    return data.sample()['city'].values[0]

def get_random_country():
    return random.choice(data.country.unique())

def get_random_city_by_country(country):
    dataframe = pd.DataFrame(data)
    country_cities = dataframe[dataframe['country'] == country.title()]
    try:
        return country_cities.sample()['city'].values[0]
    except ValueError:
        print("Country not found")

