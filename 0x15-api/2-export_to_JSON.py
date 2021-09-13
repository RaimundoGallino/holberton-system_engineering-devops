#!/usr/bin/python3

"""
for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
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
    task_dict = {}

    for i in range(num_of_tasks):
        task_dict["task"] = r.json()[i]['title']
        task_dict["completed"] = r.json()[i]['completed']
        task_dict["username"] = u.json()[0]['username']
        task_list.append(task_dict)

    new_dict = {argv[1]: task_list}

    with open(argv[1] + '.json', 'w') as f:
        json.dump(new_dict, f)
