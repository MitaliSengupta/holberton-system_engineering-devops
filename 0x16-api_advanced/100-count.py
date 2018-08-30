#!/usr/bin/python3
"""
function that prints sorted counts of given keywords
"""
import requests


def count_words(subreddit, word_list, counts={}, after=""):
    """
    recursive function that prints sorted counts of given
    keywords
    """
    url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    if after:
        url = "{}&after={}".format(url, after)
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        print_counts(counts)
        return
    req = req.json()
    if 'data' in req:
        data = req.get('data')
        if not data.get('children'):
            return (hot_list)
        for post in data.get('children'):
            for keyword in post.get('data').get('title').lower().split():
                if keyword in word_list:
                    if keyword in counts:
                        counts[keyword] += 1
                    else:
                        counts[keyword] = 1
        if not data.get('after'):
            print_counts(counts)
        else:
            count_words(subreddit, word_list, counts, data.get('after'))
    else:
        print_counts(counts)


def print_counts(counts):
    """
        Sort and print counts
    """
    if not counts:
        return
    rev_counts = {}
    for key, value in counts.items():
        rev_counts[value] = key
    for key in sorted(rev_counts, reverse=True):
        print("{}: {:d}".format(rev_counts[key], key))
