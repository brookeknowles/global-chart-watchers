import React, { useState, useEffect } from "react";
import axios from "axios";
import "./OfficialChartsPage.css";

const countryOptions = [
  { value: "", label: "Select a country" },
  { value: "au", label: "Australia" },
  { value: "ca", label: "Canada" },
  { value: "fr", label: "France" },
  { value: "ie", label: "Ireland" },
  { value: "nz", label: "New Zealand" },
  { value: "gb", label: "UK" },
  { value: "us", label: "US" },
];

function OfficialChartsPage() {
  const [chartData, setChartData] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState("");

  useEffect(() => {
    // Fetch chart data from the API endpoint based on the selected country
    if (selectedCountry) {
      axios.get(`http://127.0.0.1:5000/officialcharts/${selectedCountry}`)
        .then((response) => {
            console.log(chartData)
          setChartData(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    } else {
      // Reset chart data when no country is selected
      setChartData([]);
    }
  }, [selectedCountry]);

  const handleCountryChange = (event) => {
    setSelectedCountry(event.target.value);
  };

  return (
    <div className="official-charts-container">
      <h2 className="chart-title">Official Charts</h2>
      <select value={selectedCountry} onChange={handleCountryChange}>
        {countryOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <table>
        <thead>
          <tr>
            <th>Position</th>
            <th>Artist</th>
            <th>Track</th>
          </tr>
        </thead>
        <tbody>
          {chartData.map((item) => (
            <tr key={item.id}>
              <td>{item.Position}</td>
              <td>{item.Artist}</td>
              <td>{item.Track}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default OfficialChartsPage;
