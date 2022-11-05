#!/usr/bin/python3
"""
Query Reddit API recursively for all hot articles of a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        return all hot articles for a given subreddit
        return None if invalid subreddit given
        NOTE: the after arg is there for subsequent call of the function
    """

    # setting a custom user agent
    # https://stackoverflow.com/questions/10606133/ -->
    # sending-user-agent-using-requests-library-in-python
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get('https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code == 200:
        json = r.json()
        data_dict = json.get('data')
        post_list = data_dict.get('children')
        for post in post_list:
            post_data_dict = post.get('data')
            hot_list.append(post_data_dict.get('title'))
        after = data_dict.get('after')
        if data_dict.get('after') is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
