import requests
from typing import Dict, List

from flask import Flask, Response, jsonify
from flask_cors import CORS

from firebase_utils import db
from official_charts.au import get_australia_singles_chart
from official_charts.ca import get_canada_singles_chart
from official_charts.fr import get_france_singles_chart
from official_charts.ie import get_ireland_singles_chart
from official_charts.nz import get_nz_singles_chart
from official_charts.uk import get_uk_singles_chart
from official_charts.us import get_us_singles_chart


# Flask setup
app = Flask(__name__)
CORS(app, resources={r"/officialcharts/*": {"origins": "*"}})


def update_chart_data() -> None:
    """
    Updates the chart data in the Cloud Firestore database.
    """
    nz_data = get_nz_singles_chart()
    au_data = get_australia_singles_chart()
    us_data = get_us_singles_chart()
    ca_data = get_canada_singles_chart()
    ie_data = get_ireland_singles_chart()
    uk_data = get_uk_singles_chart()
    fr_data = get_france_singles_chart()

    chart_data = {
        'NZ': nz_data[0],
        'US': us_data[0],
        'AU': au_data[0],
        'CA': ca_data[0],
        'IE': ie_data[0],
        'GB': uk_data[0],
        'FR': fr_data[0],
    }

    # Store chart data in Cloud Firestore
    doc_ref = db.collection('charts').document('number_ones')
    doc_ref.set(chart_data)


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
