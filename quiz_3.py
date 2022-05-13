import requests
import sqlite3
import json

connection = sqlite3.connect("tvseries.db")
cursor = connection.cursor()
creating_database = '''CREATE TABLE IF NOT EXISTS  tv_series(word VARCHAR(45),seriesquantity integer)'''
cursor.execute(creating_database)
word = input("input word:")
response = requests.get(f"https://api.tvmaze.com/search/shows?q={word}")
data = json.loads(response.text)
print(f"movie names containing word {word}:")
for each in data:
    print(each)
inserting_data = ''' insert into tv_series(word,seriesquantity) values (?,?)'''
values = (word, len(data))
cursor.execute(inserting_data, values)
connection.commit()
print("information was inserted")

print("your information in database")
read_data = cursor.execute("select * from tv_series").fetchall()
for each in read_data:
    print(each)

