#!/usr/bin/python3


import requests
from sys import argv


user_name = requests.get(f"https://jsonplaceholder.\
typicode.com/users?id={argv[1]}").json()[0]['name']

todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}").json()

total = len(todos)
completed = 0
titles = ""
for i in todos:
    if i['completed']:
        completed += 1
        titles += "\t" + i['title'] + "\n"

print("Employee {} is done with tasks({}/{})"
      .format(user_name, completed, total))
print(titles[:-1])