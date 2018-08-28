#!/usr/bin/python3
import csv
import requests
from sys import argv
"""
accessing a url with employee ID to return information
"""


if __name__ == "__main__":
    """
    function to export the data into
    csv file
    """
    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    with open("{}.csv".format(ID), 'w') as csvf:
        filler = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            filler.writerow([ID, user.get('username'),
                            task.get('completed'), task.get('title')])
