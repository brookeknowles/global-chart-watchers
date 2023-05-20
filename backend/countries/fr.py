"""
France chart data
"""

from typing import Dict, List, Union

import requests
from bs4 import BeautifulSoup


from typing import List, Dict, Union
import requests
from bs4 import BeautifulSoup

def get_france_singles_chart() -> List[Dict[str, Union[str, int]]]:
    """ 
    Gets the data from the France top 100 website and returns an object with all the relevant information.
    """
    url = "https://acharts.co/france_singles_top_100"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    chart_rows = soup.select('tr[itemprop="itemListElement"]')

    chart_data = []
    for row in chart_rows:
        position = int(row.select_one('[itemprop="position"]').get_text(strip=True))
        artist = row.select_one('[itemprop="byArtist"] [itemprop="name"]').get_text(strip=True)
        song = row.select_one('[itemprop="item"] [itemprop="url"] [itemprop="name"]').get_text(strip=True)

        chart_data.append({'Position': position, 'Artist': artist, 'Track': song})

    return chart_data

