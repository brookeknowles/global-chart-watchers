import React, { useEffect, useRef } from "react";
import "./Map.css";
import jsVectorMap from "jsvectormap";
import "jsvectormap/dist/maps/world-merc.js";

function Map() {
  const mapRef = useRef();

  useEffect(() => {
    const mapElement = mapRef.current;
    const map = new jsVectorMap({
      selector: mapElement,
      map: "world_merc"
    });

    return () => {
      map.destroy();
      mapElement.innerHTML = "";
    };
  }, []);

  return (
    <div className="map-container">
      <div className="jvm-container" ref={mapRef} />
    </div>
  );
  
}

export default Map;
