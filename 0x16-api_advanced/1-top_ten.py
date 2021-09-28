#!/usr/bin/python3
'''Request subs number of given subreddit'''

import requests


def top_ten(subreddit):
    '''Request subs number of given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json?limt=10'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    if req.status_code == 200:
        r = req.json()['data']['children']
        for i in range(10):
            print(r[i]['data']['title'])
    else:
        print(None)
