employees = [
{"name": "Anna Petrova", "year": 2022, "salary": 2200},
{"name": "Ivan Sidorov", "year": 2021, "salary": 1500},
{"name": "Petr Ivanov", "year": 2020, "salary": 1200},
{"name": "Ivan Sidorov", "year": 2022, "salary": 1700},
{"name": "Olga Smirnova", "year": 2023, "salary": 2800},
{"name": "Anna Petrova", "year": 2023, "salary": 2500},
{"name": "Petr Ivanov", "year": 2021, "salary": 1300},
{"name": "Ivan Sidorov", "year": 2023, "salary": 1900},
{"name": "Petr Ivanov", "year": 2022, "salary": 1350},
{"name": "Petr Ivanov", "year": 2023, "salary": 1400}
]

names = [name["name"] for name in employees]  # получаем список всех имен из словарей
years = [year["year"] for year in employees]  # получаем список всех годов из словарей
years.sort()

dict_names = {}
dict_years = {x:0 for x in years}  # для сортировки годов

for emp in employees: 
    name = emp["name"]  # получаем имя
    year = emp["year"]  # получаем год
    dict_names[name] = dict_names.get(name, 0) + emp["salary"] / names.count(name)  # сумма каждого, деленного на число = обшая сумма поделить на число
    dict_years[year] = dict_years.get(year, 0) + emp["salary"] / years.count(year)  # сумма каждого, деленного на число = обшая сумма поделить на число

print("Средняя зарплата по сотрудникам:")
print(dict_names)
print("Средняя зарплата по годам:")
print(dict_years)
