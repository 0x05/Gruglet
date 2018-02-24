import env_loader
import requests
import logger

API_URL = 'https://ws.audioscrobbler.com/2.0/'
LASTFM_KEY = env_loader.LASTFM_KEY


# Get similar artists from last.fm
def get_similar(artist, limit, ca_log):

    params = dict(
        method='artist.getsimilar',
        artist=artist,
        api_key=LASTFM_KEY,
        format='json',
        limit=limit
    )
    response = requests.get(API_URL, params)
    data = response.json()

    try:
        similar = ', '.join(data['similarartists']['artist'][x]['name'] for x in range(limit))
    except Exception as e:
        similar = logger.log(type(e).__name__, ca_log)

    return similar


# Get top tracks for an artist from last.fm
def get_top_tracks(artist, limit, ca_log, select = -1):
    params = dict(
        method='artist.gettoptracks',
        artist=artist,
        api_key=LASTFM_KEY,
        format='json'
    )
    response = requests.get(API_URL, params)
    data =response.json()

    try:
        if select != -1:
            track = data['toptracks']['track'][select]['name']
        else:
            track = ', '.join(data['toptracks']['track'][x]['name'] for x in range(limit))
    except Exception as e:
        track = logger.log(type(e).__name__, ca_log)

    return track


# Link to last.fm wiki
def get_artist(artist):
    artist = artist.replace(' ', '+')
    wiki_url = f'<https://www.last.fm/music/{artist}/+wiki>'
    return wiki_url


