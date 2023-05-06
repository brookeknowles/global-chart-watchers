from flask import Blueprint
from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Union

au_top_50_blueprint = Blueprint('au_top_50', __name__)

@au_top_50_blueprint.route('/officialcharts/au', methods=['GET'])
def get_aria_top_50():
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
