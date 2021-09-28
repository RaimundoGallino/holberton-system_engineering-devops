#!/usr/bin/python3
'''Request subs number of given subreddit'''

import requests


def number_of_subscribers(subreddit):
    '''Request subs number of given subreddit'''
    req = requests.get('https://www.reddit.com/r/{}.json'.format(subreddit),
                       headers={'User-agent': 'your bot 0.1'})
    if req.status_code == 200:
        r = req.json()
        return r['data']['children'][0]['data']['subreddit_subscribers']
    return 0
