from flask import Flask
from flask_cors import CORS
from typing import List, Dict
from official_charts.nz import get_nz_singles_chart, nz_blueprint
from official_charts.au import get_australia_singles_chart, australia_blueprint
from official_charts.us import get_us_singles_chart, us_blueprint
from official_charts.ca import get_canada_singles_chart, canada_blueprint
from official_charts.ie import get_ireland_singles_chart, ireland_blueprint
from official_charts.uk import get_uk_singles_chart, uk_blueprint

app = Flask(__name__)
CORS(app, resources={r"/officialcharts/*": {"origins": "*"}})
app.register_blueprint(nz_blueprint)
app.register_blueprint(australia_blueprint)
app.register_blueprint(us_blueprint)
app.register_blueprint(canada_blueprint)
app.register_blueprint(ireland_blueprint)
app.register_blueprint(uk_blueprint)


@app.route('/officialcharts', methods=['GET'])
def get_all_number_ones() -> List[Dict[str, str]]:
    """
    This endpoint returns a list of dictionaries that represent the #1 song in each country
    """
    nz_data = get_nz_singles_chart()
    au_data = get_australia_singles_chart()
    us_data = get_us_singles_chart()
    ca_data = get_canada_singles_chart()
    ie_data = get_ireland_singles_chart()
    uk_data = get_uk_singles_chart()

    data = [
                {
                    "CountryCode": "NZ",
                    "Artist": nz_data[0]['Artist'],
                    "Track": nz_data[0]['Track']
                },
                {
                    "CountryCode": "US",
                    "Artist": us_data[0]['Artist'],
                    "Track": us_data[0]['Track']
                },
                {
                    "CountryCode": "AU",
                    "Artist": au_data[0]['Artist'],
                    "Track": au_data[0]['Track']
                },
                {
                    "CountryCode": "CA",
                    "Artist": ca_data[0]['Artist'],
                    "Track": ca_data[0]['Track']
                },
                {
                    "CountryCode": "IE",
                    "Artist": ie_data[0]['Artist'],
                    "Track": ie_data[0]['Track']
                },
                {
                    "CountryCode": "GB",
                    "Artist": uk_data[0]['Artist'],
                    "Track": uk_data[0]['Track']
                },
            ]
    return data


# Running app
if __name__ == '__main__':
	app.run(debug=True)
