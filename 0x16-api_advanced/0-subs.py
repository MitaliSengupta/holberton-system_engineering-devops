#!/usr/bin/python3
import requests
"""
function that queries reddit api and returns number
of subs
"""


def number_of_subscribers(subreddit):
    """
    function definition of getting number of subs
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        return (0)
    req = req.json()
    if "data" in req:
        return (req.get("data").get("subscribers"))
    else:
        return (0)
