#!/usr/bin/python3

"""
    `Export to JSON` module
"""


if __name__ == "__main__":

    import json
    import requests

    new_dict = {}

    user_list = requests.get(f"https://jsonplaceholder.\
typicode.com/users/").json()

    for user in user_list:
        todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={user.get('id')}").json()
        new_list = []
        for todo in todos:
            new_list.append({'username': user.get('username'),
                             'task': todo.get('title'),
                             'completed': todo.get('completed')})
        new_dict[user.get('id')] = new_list
    json.dump(new_dict, open(f"todo_all_employees.json", "w"))
