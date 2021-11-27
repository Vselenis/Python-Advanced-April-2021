countries = input().split(", ")
capital_cities = input().split(", ")

[print(f"{key} -> {value}") for key, value in (dict(zip(countries, capital_cities))).items()]