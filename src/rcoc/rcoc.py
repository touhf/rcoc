import csv, random
from importlib import resources

# initializing path to csv file
file_path = ''
with resources.path('data', 'cities.csv') as df:
    file_path = df

print(file_path)
file_path = str(file_path)[:-10] + 'rcoc/data/cities.csv'
print(file_path)


def read_data() -> list:
    '''Reads "cities.csv" file and returns random [city, country] entity as list
    Used by:
        1. get_random_location()
        2. get_random_country()
        3. get_random_city()
    '''
    with open(file_path) as data:
        reader = csv.reader(data)
        location = random.choice(list(reader))
        data.close()
        return location

def get_random_location() -> str:
    '''Calls read_data() to get random row from csv file
    returns random "city, location" as string
    '''
    location = read_data()
    return "{0}, {1}".format(location[0], location[1])

def get_random_country() -> str:
    '''Calls read_data() to get random row from csv file
    returns random country as string
    '''
    location = read_data()
    return location[1]

def get_random_city() -> str:
    '''Calls read_data() to get random row from csv file
    returns random city as string
    '''
    location = read_data()
    return location[0]

def get_random_city_by_country(country: str) -> str:
    '''Takes country name as argument
    Reads "cities.csv" file, filters records where country equals to argument
    returns random city from specified countrty as a string

    if specified country not found returns empty string
    '''
    data = open(file_path)
    reader = csv.reader(data)
    filtered = filter(lambda p: country.title() == p[1], reader)
    try:
        res = random.choice(list(filtered))[0]
        data.close()
        return res
    except IndexError:
        data.close()
        return ""

