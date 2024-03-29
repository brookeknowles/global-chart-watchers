"""
Australia chart data
"""

from typing import Dict, List, Union

import requests
from bs4 import BeautifulSoup

from streaming_data.apple_music import apple_music
from streaming_data.spotify import spotify
from streaming_data.youtube import youtube


def get_australia_singles_chart() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the ARIA top 50 singles website, and then returns an object with all the relevant
    information
    """

    url = "https://www.aria.com.au/charts/singles-chart"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.findAll("a", {"class": "c-chart-item__title"})
    song_list = []
    for element in song_list_raw:
        song_list.append(element.string)

    artist_list_raw = soup.findAll("a", {"class": "c-chart-item__artist"})
    artist_list = []
    for element in artist_list_raw:
        artist_list.append(element.string)

    position_list = [i for i in range(1, 100 + 1)]

    chart_data = [{'Position': positions, 'Artist': artists, 'Track': songs} for positions, artists, songs in
                  zip(position_list, artist_list, song_list)]

    return chart_data

def get_australia_spotify_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = spotify.get_spotify_chart("AU")
    return chart_data

def get_australia_apple_music_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = apple_music.get_apple_music_charts("AU")
    return chart_data

def get_australia_youtube_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = youtube.get_youtube_charts("AU")
    return chart_data
