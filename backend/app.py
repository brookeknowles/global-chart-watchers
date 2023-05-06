from typing import List, Dict

from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from official_charts.au import get_australia_singles_chart, australia_blueprint
from official_charts.ca import get_canada_singles_chart, canada_blueprint
from official_charts.ie import get_ireland_singles_chart, ireland_blueprint
from official_charts.nz import get_nz_singles_chart, nz_blueprint
from official_charts.uk import get_uk_singles_chart, uk_blueprint
from official_charts.us import get_us_singles_chart, us_blueprint


# Firebase db setup
cred = credentials.Certificate('global-chart-watchers-firebase-adminsdk-av0zu-8c70f19b28.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Flask setup
app = Flask(__name__)
CORS(app, resources={r"/officialcharts/*": {"origins": "*"}})

# Register blueprints
app.register_blueprint(nz_blueprint)
app.register_blueprint(australia_blueprint)
app.register_blueprint(us_blueprint)
app.register_blueprint(canada_blueprint)
app.register_blueprint(ireland_blueprint)
app.register_blueprint(uk_blueprint)


def update_chart_data():
    """
    Updates the chart data in the Cloud Firestore database.
    """
    nz_data = get_nz_singles_chart()
    au_data = get_australia_singles_chart()
    us_data = get_us_singles_chart()
    ca_data = get_canada_singles_chart()
    ie_data = get_ireland_singles_chart()
    uk_data = get_uk_singles_chart()

    chart_data = {
        'NZ': nz_data[0],
        'US': us_data[0],
        'AU': au_data[0],
        'CA': ca_data[0],
        'IE': ie_data[0],
        'GB': uk_data[0]
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
        data = []

    return jsonify(data)


@app.route('/updatecharts', methods=['POST'])
def update_charts():
    """
    This endpoint triggers the update of chart data in the Cloud Firestore database.
    """
    update_chart_data()
    return jsonify({'message': 'Chart data updated successfully.'})


# Running app
if __name__ == '__main__':
    app.run(debug=True)
