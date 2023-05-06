"""
Ireland chart data
"""

from flask import Blueprint
from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Union

ireland_blueprint = Blueprint('ireland_chart', __name__)

@ireland_blueprint.route('/officialcharts/ie', methods=['GET'])
def get_ireland_singles_chart() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the Ireland top 50 website, and then returns an object with 
    all the relevant information 
    """
    url = "https://www.officialcharts.com/charts/irish-singles-chart/"
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
