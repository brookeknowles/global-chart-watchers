"""
New Zealand chart data
"""

from typing import Dict, List, Union

import requests
from bs4 import BeautifulSoup

from streaming_data.apple_music import apple_music
from streaming_data.spotify import spotify
from streaming_data.youtube import youtube


def get_nz_singles_chart() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the NZTop40 website, and then returns an object with 
    all the relevant information 
    """
    url = "https://nztop40.co.nz/chart/singles"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.findAll("h2", {"class": "title"})
    song_list = [element.string for element in song_list_raw]

    artist_list_raw = soup.findAll("h3", {"class": "artist"})
    artist_list = [element.string for element in artist_list_raw]

    position_list = [i for i in range(1, 40 + 1)]

    chart_data = [{'Position': position, 'Artist': artist, 'Track': song} for position, artist, song in
                  zip(position_list, artist_list, song_list)]

    return chart_data

def get_nz_spotify_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = spotify.get_spotify_chart("NZ")
    return chart_data

def get_nz_apple_music_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = apple_music.get_apple_music_charts("NZ")
    return chart_data

def get_nz_youtube_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = youtube.get_youtube_charts("NZ")
    return chart_data
