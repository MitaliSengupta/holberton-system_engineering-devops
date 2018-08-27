#!/usr/bin/python3
import requests
from sys import argv
import csv
"""
accessing a url with employee ID to return information
"""


if __name__ == "__main__":
    """
    function to export the data into
    csv file
    """
    ID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID), verify=False).json()
    with open("{}.csv".format(ID), 'w', newline='') as csvf:
        filler = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for task in todo:
            filler.writerow([int(ID), user.get('username'),
                            task.get('completed'), task.get('title')])
