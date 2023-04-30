import React, { useState, useEffect } from "react";
import "./Map.css";
import { data } from "./mapData.js";
import WorldMap from "react-svg-worldmap";
import axios from 'axios';

function Map() {

  useEffect(() => {
    axios.get('http://localhost:3001/api/top40')
      .then((response) => {
        response.data.forEach((song) => {
          console.log(song.rank, song.title);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div className="map-container">
      <WorldMap
        color="red"
        size="lg"
        data={data}
      />
    </div>
  );
}

export default Map;
