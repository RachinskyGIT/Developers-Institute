import requests
import sqlite3
import random

# set up connection to SQLite database
conn = sqlite3.connect('.\countries\countries17.db')
c = conn.cursor()



# create table to store countries
c.execute('''CREATE TABLE IF NOT EXISTS countries
             (id INTEGER PRIMARY KEY,
              name TEXT,
              capital TEXT,
              flag TEXT,
              languages TEXT,
              subregion TEXT,
              population TEXT)''')

# send GET request to API endpoint
response = requests.get('https://restcountries.com/v2/all')

# parse response data and extract country information
countries = []
for country_data in response.json():
    name = country_data['name']
    try:
        capital =  f"capital: {country_data['capital']}"
    except:
        capital = f"capital: {None}"
    flag = country_data['flags']['png']
    languages =  f"languages: {'; '.join([lang['name'] for lang in country_data['languages']])}"
    subregion = f"subregion: {country_data['subregion']}" 
    population =  country_data['population']
    countries.append((name, capital, flag, languages, subregion, f'pop: {round(population/1000000, 3)} million people')) 

# randomly select 10 countries
selected_countries = random.sample(countries, 10)

# insert countries into database
for i, country in enumerate(selected_countries):
    c.execute("INSERT INTO countries VALUES (?, ?, ?, ?, ?, ?, ?)", 
              (i+1, country[0], country[1], country[2], country[3], country[4], country[5])) 

# commit changes and close connection
conn.commit()


# Выполняем запрос на выборку данных
c.execute("SELECT * FROM countries")

# Получаем результат запроса
result = c.fetchall()

# Выводим результат на экран
for row in result:
    print(row)

# Закрываем соединение с базой данных
conn.close()



# import requests
# import random
# import psycopg2
# ​
# HOSTNAME = "localhost"
# USERNAME = "postgres"
# PASSWORD = "271828"
# DATABASE = "di-countries"
# PORT = 5433
# ​
# connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE, port=PORT)
# ​
# url = "https://restcountries.com/v3.1/all"
# ​
# def get_data(url):
#     response = requests.get("https://restcountries.com/v3.1/all")
#     return response.json()
# ​
# def get_random_countries(data, amount):
#     return random.choices(data, k=amount)
# ​
# def informations(country):
#     name = country['name']['common']
#     try:
#         capital = country['capital'][0].replace("'", "''")
#     except:
#         capital = None
#     flag_image = country['flags']['svg']
#     try:
#         flag_alt = country['flags']['alt'].replace("'", "''")
#     except:
#         flag_alt = None
#     subregion = country['subregion']
#     population = country['population']
    
#     return name, capital, flag_image, flag_alt, subregion, population
# ​
# def string_checker(value):
#     if isinstance(value, int):
#         return value
#     return "NULL" if (not value) else f'\'{value}\''
# ​
# def insert_query(table, data):
#     name, capital, flag_image, flag_alt, subregion, population = map(string_checker, data)
# ​
#     query = f"INSERT INTO {table} (name, capital, flag_image, flag_alt, subregion, population) \
#             VALUES \
#             ({name}, {capital}, {flag_image}, {flag_alt}, {subregion}, {population}) "
    
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         connection.commit()
# ​
# response = get_data(url)
# countries = get_random_countries(response, 10)
# for country in countries:
#     insert_query("country", informations(country))
#     print(f"{country['name']['common']} added to the table")