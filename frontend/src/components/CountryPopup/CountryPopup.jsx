import React from "react";
import "./CountryPopup.css";
import { Spotify, Youtube } from '@styled-icons/boxicons-logos'
import { Applemusic } from '@styled-icons/simple-icons'
import ReactCountryFlag from "react-country-flag"
import countryCodes from "./countryCodes.js";

function CountryPopup({ countryCode, onClose }) {
  return (
    <div className="country-popup">
      <div className="popup-header">
        <h1 className="country-name">{countryCodes[countryCode]}</h1>
        <button className="close-button" onClick={onClose}>
          X
        </button>
      </div>
      <hr className="line" />
      <div className="official-chart-container">
        <h2 className="official-chart-title">Official Chart</h2>
        <hr className="line" />
        <div className="official-top3-container">
        <ReactCountryFlag 
          countryCode={countryCode} 
          svg
          style={{
            width: '2em',
            height: '2em',
          }}
          className="flag-icon"
        />
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>
      </div>
      <hr className="line" />
      <div className="streaming-container">
        <h2 className="streaming-title">Streaming</h2>
        <hr className="line" />
        <div className="spotify-container">
          <Spotify className="spotify-icon"/>
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>
        <hr className="line" />
        <div className="apple-music-container">
          <Applemusic className="apple-icon"/>
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>
        <hr className="line" />
        <div className="youtube-container">
          <Youtube className="youtube-icon"/>
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>
        <hr className="line" />

      </div>
      

    </div>
  );
}

export default CountryPopup;
