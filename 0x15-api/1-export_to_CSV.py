#!/usr/bin/python3
"""
for a given employee ID, 
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(argv[1]))
    u = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                    .format(argv[1]))

    name = u.json()[0]['name']
    completed = 0
    num_of_tasks = len(r.json())
    task_list = []

    for i in range(num_of_tasks):
        task_list.append(r.json()[i]['title'])

        if (r.json()[i]['completed'] is True):
            completed += 1

    with open(f"{argv[1]}.csv", "w") as f:
        for i in task_list:
            f.write(i)
