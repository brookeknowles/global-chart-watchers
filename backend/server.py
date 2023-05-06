from flask import Flask
from flask_cors import CORS
from typing import List, Dict
from official_charts.nz import get_NZ_top_40, nz_top_40_blueprint

app = Flask(__name__)
CORS(app, resources={r"/officialcharts/*": {"origins": "*"}})
app.register_blueprint(nz_top_40_blueprint)


@app.route('/officialcharts', methods=['GET'])
def get_all_number_ones() -> List[Dict[str, str]]:
    """
    This endpoint returns a list of dictionaries that represent the #1 song in each country
    """
    # TODO get rid of this dummy data and use the actual countries data
    nz_data = get_NZ_top_40()  # Retrieve data from the NZ chart endpoint

    data = [
                {
                    "CountryCode": "NZ",
                    "Artist": nz_data[0]['Artist'],
                    "Track": nz_data[0]['Track']
                },
                {
                    "CountryCode": "US",
                    "Artist": "Artist 2",
                    "Track": "Track 2"
                },
                {
                    "CountryCode": "GB",
                    "Artist": "Artist 3",
                    "Track": "Track 3"
                },
            ]
    return data


# Running app
if __name__ == '__main__':
	app.run(debug=True)
