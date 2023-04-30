import React from "react";
import "./Map.css";
import { data } from "./mapData.js";
import WorldMap from "react-svg-worldmap";

function Map() {

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
