import csv, random

def read_data():
    with open('./cities.csv') as data:
        reader = csv.reader(data)
        location = random.choice(list(reader))
        return location

def get_random_location():
    location = read_data()
    return "{0}, {1}".format(location[0], location[1])

def get_random_country():
    location = read_data()
    return location[1]

def get_random_city():
    location = read_data()
    return location[0]

def get_random_city_by_country(country):
    reader = csv.reader(open('./cities.csv'))
    filtered = filter(lambda p: country.title() == p[1], reader)
    try:
        return random.choice(list(filtered))[0]
    except IndexError:
        print("Country not found")

