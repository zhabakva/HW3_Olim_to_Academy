import re

try:
    f = open('cities.txt', 'r')
    s = f.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
lines = s.split('\n')
try:
    min_population = int(input("Enter the minimal accepted population"))
except ValueError:
    print("Invalid input. Please enter a valid integer for the population.")
    min_population = 0

dictionary = {"Noname": -1}
for line in lines:
    city = line.split(':')[0]
    population = line.split(':')[1]
    city_new = re.sub(r'[^\w\s]', '', city)
    population_new = int(re.sub(r'[^\w\s]', '', population))
    dictionary.update({str(city_new): int(population_new)})
filtered_cities = {city: population for city, population in dictionary.items() if population > min_population}
sorted_dict = dict(sorted(filtered_cities.items()))
try:
    with open(r"filtered_cities.txt", "w") as file:
        for key in sorted_dict.keys():
            file.write(f"{key},':',{sorted_dict[key]}\n")

except IOError as e:
    print(f"Error: Unable to write to file")
