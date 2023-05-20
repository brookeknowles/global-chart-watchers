/**
This function gets data from each country's official charts and returns an object 
containing the chart data.

@return {Object|null} - An object containing the chart data for each country, where the keys 
                        are the country codes in uppercase and the values are the chart data 
                        objects. Returns null if an error occurs during the fetch operation.

e.g:
{
  "NZ": {
    "CountryCode": "NZ",
    "Artist": "Artist 1",
    "Track": "Track 1"
  },
  "US": {
    "CountryCode": "US",
    "Artist": "Artist 2",
    "Track": "Track 2"
  },
  "GB": {
    "CountryCode": "GB",
    "Artist": "Artist 3",
    "Track": "Track 3"
  }
}

*/
export const fetchChartData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/numberones");
      const data = await response.json();
      const chartData = {};
  
      if (Array.isArray(data)) {
        data.forEach(item => {
          const countryCode = item.CountryCode.toUpperCase();
          chartData[countryCode] = item;
        });
      }
  
      return chartData;
    } catch (error) {
      console.error("Error fetching chart data:", error);
    }
    return null;
  };
  