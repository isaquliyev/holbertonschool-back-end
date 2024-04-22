#!/usr/bin/python3

"""
    The `Gather data from an API` module
"""


if __name__ == "__main__":

    import requests
    from sys import argv
    
    try:
        user_name = requests.get(f"https://jsonplaceholder.\
typicode.com/users?id={argv[1]}").json()[0]['name']
    except Exception:
        user_name = ""
    
    try:
        todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}").json()
    except Exception:
        todos = []

    total = len(todos)
    completed = 0
    titles = ""
    for i in todos:
        if i['completed']:
            completed += 1
            titles += "\t" + i['title'] + "\n"

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed, total))
    print(titles[:-1])
