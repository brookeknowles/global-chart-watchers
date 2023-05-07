import React, { useState } from "react";
import Header from "./components/Header/Header";
import Navbar from "./components/Navbar/Navbar";
import Map from "./components/Map/Map";
import Footer from "./components/Footer/Footer";
import CountryPopup from "./components/CountryPopup/CountryPopup";
import "./App.css";

function App() {
  const [selectedCountry, setSelectedCountry] = useState(null);

  const handleCountryClick = (countryName) => {
    setSelectedCountry(countryName);
  };

  const handleClosePopup = () => {
    setSelectedCountry(null);
  };

  return (
    <div className="App">
      <Header />
      <Navbar />
      <div className="map-container">
        <Map onCountryClick={handleCountryClick} />
      </div>
      <div className="country-popup-container">
        {selectedCountry && (
          <CountryPopup
            countryName={selectedCountry}
            onClose={handleClosePopup}
          />
        )}
      </div>
      <Footer />
    </div>
  );
}

export default App;
