#!/usr/bin/python3

"""
for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get('https://jsonplaceholder.typicode.com/users')

    new_dict = {}
    for i in r.json():
        task_list = []
        u = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(i['id']))
        for j in range(0, len(u.json())):
            task_dict = {}
            task_dict["username"] = i['username']
            task_dict["task"] = u.json()[j]['title']
            task_dict["completed"] = u.json()[j]['completed']
            task_list.append(task_dict)
        new_dict[i['id']] = task_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(new_dict, f)
