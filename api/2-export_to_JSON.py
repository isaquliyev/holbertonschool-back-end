#!/usr/bin/python3

"""
    `Export to JSON` module
"""


if __name__ == "__main__":

    import json
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    new_dict = {}
    new_list = []

    username = requests.get(f"https://jsonplaceholder.\
typicode.com/users/{argv[1]}").json().get('username')

    todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}").json()
    for todo in todos:
        new_list.append({'task': todo.get('title'),
                         'completed': todo.get('completed'),
                         'username': username})
    new_dict[str(argv[1])] = new_list
    json.dump(new_dict, open(f"{argv[1]}.json", "w"))
