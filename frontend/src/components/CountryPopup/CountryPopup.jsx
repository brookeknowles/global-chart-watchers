import React from "react";
import "./CountryPopup.css";
import { Spotify, Youtube } from '@styled-icons/boxicons-logos'
import { Applemusic } from '@styled-icons/simple-icons'

// idea for layout on figma

function CountryPopup({ countryCode, onClose }) {
  return (
    <div className="country-popup">
      <div className="popup-header">
        <h1>{countryCode}</h1> {/* TODO figure out how to make this say the country not the code */}
        <button className="close-button" onClick={onClose}>
          X
        </button>
      </div>

      <div className="official-chart-container">
        <h2 className="official-chart-title">Official Chart</h2>
        <div className="official-top3-container">
          {/* Decide on a similar sized icon/pic to go here so it looks more consistent w streaming */}
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>
      </div>

      <div className="streaming-container">
        <h2 className="streaming-title">Streaming</h2>

        <div className="spotify-container">
          <Spotify />
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>

        <div className="apple-music-container">
          <Applemusic />
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>

        <div className="youtube-container">
          <Youtube />
          <ol type="1">
            <li>Miley Cyrus - Flowers</li>
            <li>Morgan Wallen - Last Night</li>
            <li>SZA - Kill Bill</li>
          </ol>
        </div>

      </div>
      

    </div>
  );
}

export default CountryPopup;
