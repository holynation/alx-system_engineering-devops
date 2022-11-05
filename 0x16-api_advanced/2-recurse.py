#!/usr/bin/python3
"""
Query Reddit API recursively for all hot articles of a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp", count=0):
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

    # update url each recursive call with param "after"
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "tmp":
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=headers,
                     allow_redirects=False).json()

    # validate the data in the parameters
    if "data" not in r and hot_list == []:
        return None
    # append top titles to hot_list
    results = r.get('data', {}).get('children', [])
    if not results:
        return hot_list
    for e in results:
        hot_list.append(e.get('data').get('title'))
        count += 1

    # get next param "after" else nothing else to recurse
    after = r.get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after, count))
