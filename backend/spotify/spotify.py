import requests

from playlist_ids import playlist_ids
from secrets import spotify_client_id, spotify_client_secret

spotify_url = 'https://api.spotify.com/v1/'
token_url = 'https://accounts.spotify.com/api/token'


def get_token():
    """ 
    Requests an access token from spotify API
    """
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': spotify_client_id,
        'client_secret': spotify_client_secret,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token


def get_playlist(id):
    """ 
    Accesses the Spotify API get playlists endpoint
    """
    url = f'{spotify_url}playlists/{id}'
    authorized_headers = {
        'Authorization': f'Bearer {get_token()}'
    }
    response = requests.get(url, headers=authorized_headers).json()
    return response


def get_spotify_chart(country_code):
    """
    Gets the top 50 
    """
    playlist_id = playlist_ids[country_code]
    response = get_playlist(playlist_id)
    
    track_list = []
    tracks = response['tracks']['items']
    
    for track in tracks:
        artist = track['track']['artists'][0]['name']
        track_name = track['track']['name']
        track_dict = {"Artist": artist, "Track": track_name}
        track_list.append(track_dict)
    
    return track_list
