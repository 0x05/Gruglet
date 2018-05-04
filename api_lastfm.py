import env_loader
import requests

API_URL = 'https://ws.audioscrobbler.com/2.0/'
LASTFM_KEY = env_loader.LASTFM_KEY


# Get similar artists from last.fm
def get_similar(artist, limit):
    params = dict(
        method='artist.getsimilar',
        artist=artist,
        api_key=LASTFM_KEY,
        format='json',
        limit=limit
    )
    response = requests.get(API_URL, params)
    if response.ok:
        data = response.json()
        if 'error' in data:
            return data['message']
        else:
            dnum = len(data['similarartists']['artist'])  # Number of items

            # Range check
            if limit > dnum:
                limit = dnum

            similar = ''

            if dnum > 0:
                similar = ', '.join(data['similarartists']['artist'][x]['name'] for x in range(limit))
            else:
                similar = 'No similar artists in database'
    else:
        return response.status_code

    return similar


# Get top tracks for an artist from last.fm
def get_top_tracks(artist, limit, select=-1):
    params = dict(
        method='artist.gettoptracks',
        artist=artist,
        api_key=LASTFM_KEY,
        format='json'
    )
    response = requests.get(API_URL, params)
    if response.ok:
        data = response.json()
        if 'error' in data:
            return data['message']
        else:
            dnum = len(data['toptracks']['track'])  # Number of items

            # Range check
            if limit > dnum:
                limit = dnum

            if select > dnum:
                select = dnum

            track = ''

            if dnum > 0:
                if select != -1:
                    track = data['toptracks']['track'][select]['name']
                else:
                    track = ', '.join(data['toptracks']['track'][x]['name'] for x in range(limit))
            else:
                track = 'No top tracks in database'
    else:
        return response.status_code

    return track


# Get top tracks for an artist from last.fm
def get_top_albums(artist, limit, select=-1):
    params = dict(
        method='artist.gettopalbums',
        artist=artist,
        api_key=LASTFM_KEY,
        format='json'
    )
    response = requests.get(API_URL, params)
    if response.ok:
        data = response.json()
        if 'error' in data:
            return data['message']
        else:
            dnum = len(data['topalbums']['album'])  # Number of items

            # Range check
            if limit > dnum:
                limit = dnum

            if select > dnum:
                select = dnum

            album = ''

            if dnum > 0:
                if select != -1:
                    album = data['topalbums']['album'][select]['name']
                else:
                    album = ', '.join(data['topalbums']['album'][x]['name'] for x in range(limit))
            else:
                album = 'No top albums in database'
    else:
        return response.status_code

    return album


# Get top tracks for a country from last.fm
def geott(country, limit, select=-1):
    params = dict(
        method='geo.getTopTracks',
        country=country,
        api_key=LASTFM_KEY,
        format='json'
    )
    response = requests.get(API_URL, params)
    if response.ok:
        data = response.json()
        if 'error' in data:
            return data['message']
        else:
            dnum = len(data['tracks']['track'])  # Number of items
            
            # Range check
            if limit > dnum:
                limit = dnum

            if select > dnum:
                select = dnum

            track = ''

            if dnum > 0:
                if select != -1:
                    track = data['tracks']['track'][select]['name']
                else:
                    track = ', '.join(data['tracks']['track'][x]['name'] for x in range(limit))
            else:
                track = 'No tracks for selected country in database'
    else:
        return response.status_code

    return track


# Link to last.fm wiki
def get_artist(artist):
    artist = artist.replace(' ', '+')
    wiki_url = f'<https://www.last.fm/music/{artist}/+wiki>'

    return wiki_url