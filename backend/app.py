import requests
from typing import Dict, List

from flask import Flask, Response, jsonify
from flask_cors import CORS

from firebase_utils import db
from countries.au import (
    get_australia_singles_chart, 
    get_australia_spotify_chart, 
    get_australia_apple_music_chart, 
    get_australia_youtube_chart
)
from countries.ca import (
    get_canada_singles_chart,
    get_canada_spotify_chart, 
    get_canada_apple_music_chart, 
    get_canada_youtube_chart
)
from countries.fr import (
    get_france_singles_chart,
    get_france_spotify_chart, 
    get_france_apple_music_chart, 
    get_france_youtube_chart
)
from countries.ie import (
    get_ireland_singles_chart,
    get_ireland_spotify_chart, 
    get_ireland_apple_music_chart, 
    get_ireland_youtube_chart
)
from countries.nz import (
    get_nz_singles_chart,
    get_nz_spotify_chart, 
    get_nz_apple_music_chart, 
    get_nz_youtube_chart
)
from countries.uk import (
    get_uk_singles_chart,
    get_uk_spotify_chart, 
    get_uk_apple_music_chart, 
    get_uk_youtube_chart
)
from countries.us import (
    get_us_singles_chart,
    get_us_spotify_chart, 
    get_us_apple_music_chart, 
    get_us_youtube_chart
)


# Flask setup
app = Flask(__name__)
CORS(app, resources={r"/officialcharts/*": {"origins": "*"}})


def update_chart_data() -> None:
    """
    Updates the chart data in the Cloud Firestore database.
    """
    # Get current chart data from website and/or API
    # Official charts
    nz_official_chart_data = get_nz_singles_chart()
    au_official_chart_data = get_australia_singles_chart()
    us_official_chart_data = get_us_singles_chart()
    ca_official_chart_data = get_canada_singles_chart()
    ie_official_chart_data = get_ireland_singles_chart()
    uk_official_chart_data = get_uk_singles_chart()
    fr_official_chart_data = get_france_singles_chart()

    # Spotify
    nz_spotify_data = get_nz_spotify_chart()
    au_spotify_data = get_australia_spotify_chart()
    us_spotify_data = get_us_spotify_chart()
    ca_spotify_data = get_canada_spotify_chart()
    ie_spotify_data = get_ireland_spotify_chart()
    uk_spotify_data = get_uk_spotify_chart()
    fr_spotify_data = get_france_spotify_chart()

    # Apple Music
    nz_apple_music_data = get_nz_apple_music_chart()
    au_apple_music_data = get_australia_apple_music_chart()
    us_apple_music_data = get_us_apple_music_chart()
    ca_apple_music_data = get_canada_apple_music_chart()
    ie_apple_music_data = get_ireland_apple_music_chart()
    uk_apple_music_data = get_uk_apple_music_chart()
    fr_apple_music_data = get_france_apple_music_chart()

    # YouTube
    nz_youtube_data = get_nz_youtube_chart()
    au_youtube_data = get_australia_youtube_chart()
    us_youtube_data = get_us_youtube_chart()
    ca_youtube_data = get_canada_youtube_chart()
    ie_youtube_data = get_ireland_youtube_chart()
    uk_youtube_data = get_uk_youtube_chart()
    fr_youtube_data = get_france_youtube_chart()

    number_ones = {
        'NZ': nz_official_chart_data[0],
        'US': us_official_chart_data[0],
        'AU': au_official_chart_data[0],
        'CA': ca_official_chart_data[0],
        'IE': ie_official_chart_data[0],
        'GB': uk_official_chart_data[0],
        'FR': fr_official_chart_data[0],
    }

    full_singles_charts = {
        'NZ': nz_official_chart_data,
        'US': us_official_chart_data,
        'AU': au_official_chart_data,
        'CA': ca_official_chart_data,
        'IE': ie_official_chart_data,
        'GB': uk_official_chart_data,
        'FR': fr_official_chart_data,
    }

    spotify_charts = {
        'NZ': nz_spotify_data,
        'US': us_spotify_data,
        'AU': au_spotify_data,
        'CA': ca_spotify_data,
        'IE': ie_spotify_data,
        'GB': uk_spotify_data,
        'FR': fr_spotify_data,
    }

    apple_music_charts = {
        'NZ': nz_apple_music_data,
        'US': us_apple_music_data,
        'AU': au_apple_music_data,
        'CA': ca_apple_music_data,
        'IE': ie_apple_music_data,
        'GB': uk_apple_music_data,
        'FR': fr_apple_music_data,
    }

    youtube_charts = {
        'NZ': nz_youtube_data,
        'US': us_youtube_data,
        'AU': au_youtube_data,
        'CA': ca_youtube_data,
        'IE': ie_youtube_data,
        'GB': uk_youtube_data,
        'FR': fr_youtube_data,
    }

    country_card_data = {
        'NZ': {
            'official': nz_official_chart_data[:3],
            'spotify': nz_spotify_data[:3],
            'apple_music': nz_apple_music_data[:3],
            'youtube': nz_youtube_data[:3]
        },
        'US': {
            'official': us_official_chart_data[:3],
            'spotify': us_spotify_data[:3],
            'apple_music': us_apple_music_data[:3],
            'youtube': us_youtube_data[:3]
        },
        'AU': {
            'official': au_official_chart_data[:3],
            'spotify': au_spotify_data[:3],
            'apple_music': au_apple_music_data[:3],
            'youtube': au_youtube_data[:3]
        },
        'CA': {
            'official': ca_official_chart_data[:3],
            'spotify': ca_spotify_data[:3],
            'apple_music': ca_apple_music_data[:3],
            'youtube': ca_youtube_data[:3]
        },
        'IE': {
            'official': ie_official_chart_data[:3],
            'spotify': ie_spotify_data[:3],
            'apple_music': ie_apple_music_data[:3],
            'youtube': ie_youtube_data[:3]
        },
        'GB': {
            'official': uk_official_chart_data[:3],
            'spotify': uk_spotify_data[:3],
            'apple_music': uk_apple_music_data[:3],
            'youtube': uk_youtube_data[:3]
        },
        'FR': {
            'official': fr_official_chart_data[:3],
            'spotify': fr_spotify_data[:3],
            'apple_music': fr_apple_music_data[:3],
            'youtube': fr_youtube_data[:3]
        },
    }

    # Store chart data in Cloud Firestore
    doc_ref_number_ones = db.collection('charts').document('number_ones')
    doc_ref_number_ones.set(number_ones)

    doc_ref_full_charts = db.collection('charts').document('full_singles_charts')
    doc_ref_full_charts.set(full_singles_charts)

    doc_ref_spotify_charts = db.collection('charts').document('spotify_charts')
    doc_ref_spotify_charts.set(spotify_charts)

    doc_ref_apple_music_charts = db.collection('charts').document('apple_music_charts')
    doc_ref_apple_music_charts.set(apple_music_charts)

    doc_ref_youtube_charts = db.collection('charts').document('youtube_charts')
    doc_ref_youtube_charts.set(youtube_charts)

    doc_ref_country_card_data = db.collection('charts').document('country_card_data')
    doc_ref_country_card_data.set(country_card_data)



@app.route('/officialcharts', methods=['GET'])
def get_all_number_ones() -> List[Dict[str, str]]:
    """
    This endpoint returns a list of dictionaries that represent the #1 song in each country
    """
    # Retrieve chart data from Cloud Firestore
    doc_ref = db.collection('charts').document('number_ones')
    chart_data = doc_ref.get().to_dict()

    if chart_data:
        data = [
            {
                'CountryCode': country,
                'Artist': chart_data[country]['Artist'],
                'Track': chart_data[country]['Track']
            }
            for country in chart_data
        ]
    else:
        # Call the update_charts endpoint to update the chart data
        response = requests.post('http://127.0.0.1:5000/updatecharts')
        if response.status_code == 200:
            return response.json()

        data = []

    return jsonify(data)



@app.route('/updatecharts', methods=['POST'])
def update_charts() -> Response:
    """
    This endpoint triggers the update of chart data in the Cloud Firestore database.
    """
    update_chart_data()
    
    # Make the GET request to update the data on the frontend
    response = requests.get('http://127.0.0.1:5000/officialcharts')
    if response.status_code == 200:
        return response.json()
    
    return jsonify({'message': 'Chart data updated successfully.'})


# Running app
if __name__ == '__main__':
    app.run(debug=True)
