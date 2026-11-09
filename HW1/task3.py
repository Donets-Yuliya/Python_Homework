countries = {
    "BY": "Belarus",
    "PL": "Poland",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain"
}
print(countries)

new_countries = {v: k for k, v in countries.items()}

print(new_countries)

