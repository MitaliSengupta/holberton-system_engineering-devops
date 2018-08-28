#!/usr/bin/python3
import json
import requests
from sys import argv
"""
accessing a url with employee ID to return information
"""


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    user_dict = {}
    usernamedict = {}
    for user in users:
        ID = user.get("id")
        user_dict[ID] = []
        usernamedict[ID] = user.get('username')
    for task in todo:
        task_dict = {}
        ID = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict['username'] = usernamedict.get(ID)
        user_dict.get(ID).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(user_dict, jsfile)
