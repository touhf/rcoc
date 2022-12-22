rcoc - Random Country or City
=======================================================================================
Simple script for
1. generating random city name (any country)
2. generating random country name
3. generating random city from of country
### usage
```
import rcoc

print("Random city: ", rcoc.get_random_city())

rand_country = rcoc.get_random_country()
print("\nRandom country: ", rand_country)
print("Random {0} city: {1}".format(rand_country, rcoc.get_random_city_by_country(rand_country)))
```
### output example
```
Random city:  Gagliano Aterno

Random country:  Bolivia
Random Bolivia city: Reyes
```
