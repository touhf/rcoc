import rcoc

print("Random city: ", rcoc.get_random_city())

rand_country = rcoc.get_random_country()
print("\nRandom country: ", rand_country)
print("Random {0} city: {1}".format(rand_country, rcoc.get_random_city_by_country(rand_country)))

