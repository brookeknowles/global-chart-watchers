from flask import Blueprint
from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Union

nz_top_40_blueprint = Blueprint('nz_top_40', __name__)

@nz_top_40_blueprint.route('/officialcharts/nz', methods=['GET'])
def get_NZ_top_40() -> List[Dict[str, Union[str, int]]]:
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
