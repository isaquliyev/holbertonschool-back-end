#!/usr/bin/python3

"""
    `Export to CSV` module
"""


if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}").json()
    username = requests.get(f"https://jsonplaceholder.\
typicode.com/users/{argv[1]}").json().get('username')

    csv_writer = csv.writer(open(f'{argv[1]}.csv', 'w'), quoting=csv.QUOTE_ALL)

    for todo in todos:
        csv_writer.writerow([todo.get('userId'), username,
                             todo.get('completed'), todo.get('title')])
