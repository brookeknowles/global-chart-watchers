import React from "react";
import "./CountryPopup.css";

function CountryPopup({ countryName, onClose }) {
  return (
    <div className="country-popup">
      <div className="popup-header">
        <h5>Country: {countryName}</h5>
        <button className="close-button" onClick={onClose}>
          X
        </button>
      </div>
      <div className="popup-content">
        {/* TODO */}
      </div>
    </div>
  );
}

export default CountryPopup;
