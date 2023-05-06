from flask import Blueprint
from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Union

us_hot_100_blueprint = Blueprint('us_hot_100', __name__)

@us_hot_100_blueprint.route('/officialcharts/us', methods=['GET'])
def get_billboard_hot_100() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the Billboard Hot 100 website, and then returns an object with all the relevant
    information 
    """

    url = "https://www.billboard.com/charts/hot-100/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    soup.find("div", class_="lxml")

    # stripping punctuation so spotify doesn't pack a sad. may need to add an if clause later so that I can keep
    # punctuation for display on web page
    song_list = [result.text.strip() for result in soup.select(
        "div.chart-results-list > div.o-chart-results-list-row-container > ul.o-chart-results-list-row > "
        "li:nth-child(4) > ul > li:nth-child(1) h3")]
    artist_list = [result.text.strip() for result in soup.select(
        "div.chart-results-list > div.o-chart-results-list-row-container> ul.o-chart-results-list-row > li:nth-child("
        "4) > ul > li:nth-child(1) span")]
    position_list = [i for i in range(1, 100 + 1)]

    chart_data = [{'Position': positions, 'Artist': artists, 'Track': songs} for positions, artists, songs in
                             zip(position_list, artist_list, song_list)]

    return chart_data
