"""
Ireland chart data
"""

from typing import Dict, List, Union

import requests
from bs4 import BeautifulSoup

from streaming_data.apple_music import apple_music
from streaming_data.spotify import spotify
from streaming_data.youtube import youtube


def get_ireland_singles_chart() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the Ireland top 50 website, and then returns an object with 
    all the relevant information 
    """
    url = "https://www.officialcharts.com/charts/irish-singles-chart/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.findAll("a", {"class": "chart-name font-bold inline-block"})
    song_list = [element.get_text(strip=True) for element in song_list_raw]

    artist_list_raw = soup.findAll("a", {"class": "chart-artist text-lg inline-block"})
    artist_list = [element.get_text(strip=True) for element in artist_list_raw]

    position_list = position_list = [i for i in range(1, 50 + 1)]

    chart_data = [{'Position': position, 'Artist': artist, 'Track': song} for position, artist, song in
                  zip(position_list, artist_list, song_list)]

    return chart_data

def get_ireland_spotify_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = spotify.get_spotify_chart("IE")
    return chart_data

def get_ireland_apple_music_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = apple_music.get_apple_music_charts("IE")
    return chart_data

def get_ireland_youtube_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = youtube.get_youtube_charts("IE")
    return chart_data
