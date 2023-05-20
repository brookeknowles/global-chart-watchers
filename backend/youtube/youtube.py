from typing import List, Dict, Union
import requests
from bs4 import BeautifulSoup

def get_youtube_charts(country: str) -> List[Dict[str, Union[str, int]]]:
    url = f"https://kworb.net/youtube/insights/{country.lower()}.html"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.select("#weeklytable .text.mp div")
    song_list = [element.get_text(strip=True).split(" - ")[1] for element in song_list_raw]

    artist_list_raw = [element.get_text(strip=True).split(" - ")[0] for element in song_list_raw]
    artist_list = [element.split(" - ")[0] for element in artist_list_raw]

    chart_data = []
    for index, song in enumerate(song_list):
        position = index + 1
        artist = artist_list[index]
        chart_data.append({'Position': position, 'Artist': artist, 'Track': song})

    return chart_data
