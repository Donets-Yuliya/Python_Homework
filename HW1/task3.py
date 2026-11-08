countries = {
    "BY": "Belarus",
    "PL": "Poland",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain"
}
print(countries)

new_countries = {}

for key in countries: 
    new_countries |= {countries[key] : key}

print(new_countries)
