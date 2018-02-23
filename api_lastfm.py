import env_loader
import requests
from secrets import randbelow

API_URL = 'https://ws.audioscrobbler.com/2.0/'
LASTFM_KEY = env_loader.LASTFM_KEY


# Request a number of similar artists from last.fm
def get_similar(artist,limit):

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
    except:
        similar = 'Invalid querry.'

    return similar

def get_top_tracks(artist, select):
    params = dict(
        method='artist.gettoptracks',
        artist=artist,
        api_key=LASTFM_KEY,
        format='json'
    )

    response = requests.get(API_URL, params)
    data =response.json()

    try:
        track = ', '.join(data['toptracks']['track'][x]['name'] for x in range(select))
    except:
        track = 'Out of range'

    return track

# Link to last.fm wiki. No parsing is required
def get_artist(artist, yt=0):
    wiki_url = f'https://www.last.fm/music/{artist}/+wiki'
    return wiki_url


