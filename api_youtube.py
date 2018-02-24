import env_loader
import logger
import requests

API_URL = 'https://www.googleapis.com/youtube/v3/search'
YT_URL = 'https://www.youtube.com/watch?v='
YT_KEY = env_loader.YT_KEY


def search(sq, ca_log, result):

    params = dict(
        part='snippet',
        maxResults=10,
        q=sq,
        key=YT_KEY,
        type='video'
    )
    response = requests.get(API_URL, params)
    data = response.json()

    try:
        link = YT_URL + data['items'][result]['id']['videoId']
    except Exception as e:
        link = logger.log(type(e).__name__, ca_log)

    return link
