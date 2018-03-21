import env_loader
import requests

API_URL = 'https://www.googleapis.com/youtube/v3/search'
YT_URL = 'https://www.youtube.com/watch?v='
YT_KEY = env_loader.YT_KEY


def search(sq, result):
    params = dict(
        part='snippet',
        maxResults=10,
        q=sq,
        key=YT_KEY,
        type='video'
    )
    response = requests.get(API_URL, params)
    if response.ok:
        data = response.json()
        if data['pageInfo']['totalResults'] != 0:
            link = YT_URL + data['items'][result]['id']['videoId']
        else:
            link = f'No results for \'{sq}\''
    else:
        return response.status_code

    return link
