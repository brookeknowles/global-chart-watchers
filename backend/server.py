from flask import Flask
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Union


# Initializing flask app
app = Flask(__name__)
CORS(app)

@app.route('/officialcharts/nz')
def get_NZ_top_40() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the NZTop40 website

    Returns: List of dictionaries containing chart data, e.g.:
    [
        {
            "Artist": "artistname",
            "Position": 1,
            "Track": "trackname"
        },
    ]
    """

    url = "https://nztop40.co.nz/chart/singles"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    song_list_raw = soup.findAll("h2", {"class": "title"})
    song_list = []
    for element in song_list_raw:
        song_list.append(element.string)

    artist_list_raw = soup.findAll("h3", {"class": "artist"})
    artist_list = []
    for element in artist_list_raw:
        artist_list.append(element.string)

    position_list = [i for i in range(1, 40 + 1)]

    chart_data = [{'Position': positions, 'Artist': artists, 'Track': songs} for positions, artists, songs in
                             zip(position_list, artist_list, song_list)]

    return chart_data

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
