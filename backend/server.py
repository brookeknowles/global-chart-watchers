from flask import Flask
from flask_cors import CORS
from typing import List, Dict
from official_charts.nz import get_NZ_top_40, nz_top_40_blueprint
from official_charts.au import get_aria_top_50, au_top_50_blueprint
from official_charts.us import get_billboard_hot_100, us_hot_100_blueprint

app = Flask(__name__)
CORS(app, resources={r"/officialcharts/*": {"origins": "*"}})
app.register_blueprint(nz_top_40_blueprint)
app.register_blueprint(au_top_50_blueprint)
app.register_blueprint(us_hot_100_blueprint)


@app.route('/officialcharts', methods=['GET'])
def get_all_number_ones() -> List[Dict[str, str]]:
    """
    This endpoint returns a list of dictionaries that represent the #1 song in each country
    """
    nz_data = get_NZ_top_40()
    au_data = get_aria_top_50()
    us_data = get_billboard_hot_100()

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
            ]
    return data


# Running app
if __name__ == '__main__':
	app.run(debug=True)
