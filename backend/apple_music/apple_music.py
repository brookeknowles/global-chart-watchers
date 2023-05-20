from typing import List, Dict, Union
from bs4 import BeautifulSoup
import requests

def get_apple_music_charts(countryCode: str) -> List[Dict[str, Union[str, int]]]:
    """
    Apple music
    """
    url = f"https://kworb.net/charts/apple_s/{countryCode.lower()}.html"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.select("#simpletable tbody tr .text div")
    song_list = song_list = [element.get_text(strip=True).split(" - ", 1)[1] for element in song_list_raw]

    artist_list_raw = soup.select("#simpletable tbody tr .text div")
    artist_list = [element.get_text(strip=True).split(" - ")[0] for element in artist_list_raw]

    position_list_raw = soup.select("#simpletable tbody tr td:nth-child(1)")
    position_list = [int(element.get_text(strip=True)) for element in position_list_raw]

    chart_data = [{'Position': position, 'Artist': artist, 'Track': song} for position, artist, song in
                  zip(position_list, artist_list, song_list)]

    return chart_data
