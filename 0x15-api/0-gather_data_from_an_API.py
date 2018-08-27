#!/usr/bin/python3
import requests
from sys import argv
"""
accessing a url with employee ID to return information
"""


if __name__ == "__main__":
    ID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?ID={}".
                        format(ID), verify=False).json()
    tasks = []
    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{})".
          format(user.get('name'), len(tasks), len(todo)))
    print("\n".join("\t{}".format(task) for task in tasks))
