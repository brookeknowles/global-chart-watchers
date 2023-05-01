import React, { useEffect, useRef } from "react";
import "./Map.css";
import jsVectorMap from "jsvectormap";
import "jsvectormap/dist/maps/world-merc.js";

function Map() {
  const mapRef = useRef(null);
  const map = useRef(null);

  useEffect(() => {
    const mapElement = mapRef.current;

    const regionStyle = {
      initial: {
        fill: "white",
        "fill-opacity": 1,
        stroke: "none",
        "stroke-width": 0,
        "stroke-opacity": 1
      },
      hover: {
        "fill-opacity": 0.8,
        cursor: "pointer"
      },
      selected: {
        fill: "red"
      },
      selectedHover: {}
    };

    map.current = new jsVectorMap({
      selector: mapElement,
      map: "world_merc",
      backgroundColor: "grey",
      regionsSelectable: true,
      regionsSelectableOne: true,
      regionStyle: regionStyle,
    });

    const handleResize = () => {
      if (map.current) {
        map.current.setFocus({ scale: 1, x: 0.5, y: 0.5 });
        map.current.updateSize();
      }
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
      if (map.current) {
        map.current.destroy();
        mapElement.innerHTML = "";
      }
    };
  }, []);

  return (
    <div className="map-container">
      <div className="jvm-container" ref={mapRef} />
    </div>
  );
}

export default Map;
