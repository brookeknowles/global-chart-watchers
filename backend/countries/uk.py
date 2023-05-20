"""
UK chart data
"""

from typing import Dict, List, Union

import requests
from bs4 import BeautifulSoup

from streaming_data.apple_music import apple_music
from streaming_data.spotify import spotify
from streaming_data.youtube import youtube


def get_uk_singles_chart() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the Ireland top 50 website, and then returns an object with 
    all the relevant information 
    """
    url = "https://www.officialcharts.com/charts/singles-chart/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.select(".chart-positions .title-artist .title a")
    song_list = [element.get_text(strip=True) for element in song_list_raw]

    artist_list_raw = soup.select(".chart-positions .title-artist .artist a")
    artist_list = [element.get_text(strip=True) for element in artist_list_raw]

    position_list_raw = soup.select(".chart-positions .position")
    position_list = [int(element.get_text(strip=True)) for element in position_list_raw]

    chart_data = [{'Position': position, 'Artist': artist, 'Track': song} for position, artist, song in
                  zip(position_list, artist_list, song_list)]

    return chart_data

def get_uk_spotify_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = spotify.get_spotify_chart("GB")
    return chart_data

def get_uk_apple_music_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = apple_music.get_apple_music_charts("UK")
    return chart_data

def get_uk_youtube_chart() -> List[Dict[str, Union[str, int]]]:
    chart_data = youtube.get_youtube_charts("UK")
    return chart_data