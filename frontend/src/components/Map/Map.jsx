import React, { useEffect, useRef, useState } from "react";
import "./Map.css";
import jsVectorMap from "jsvectormap";
import "jsvectormap/dist/maps/world-merc.js";
import { fetchChartData } from "./chartData";
import CountryPopup from "../CountryPopup/CountryPopup";

function Map() {
  const mapRef = useRef(null);
  const map = useRef(null);
  const [chartData, setChartData] = useState(null);
  const [selectedCountry, setSelectedCountry] = useState(null);
  const [isCountryClicked, setIsCountryClicked] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchChartData();
      setChartData(data);
    };

    fetchData();
  }, []);

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
      onRegionTooltipShow(event, tooltip, code) {
        const countryName = tooltip.text();
        let tooltipContent = `<h5>Country: ${countryName}</h5>`;

        if (chartData && chartData[code]) {
          const { Artist, Track } = chartData[code];
          tooltipContent += `<p class="text-xs">Artist: ${Artist}</p>`;
          tooltipContent += `<p class="text-xs">Track: ${Track}</p>`;
        }

        tooltip.text(tooltipContent, true); // Update tooltip content with HTML
      },
      onRegionClick(event, code) {
        setSelectedCountry(code);
        setIsCountryClicked(true);
      }
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
  }, [chartData]);

  const handleClosePopup = () => {
    setSelectedCountry(null);
    setIsCountryClicked(false);
  };

  return (
    <div className={`map-container ${isCountryClicked ? "country-clicked" : ""}`}>
      <div className="jvm-container" ref={mapRef} />
      {selectedCountry && (
        <div className="popup-overlay">
          <CountryPopup
            countryCode={selectedCountry}
            onClose={handleClosePopup}
          />
        </div>
      )}
    </div>
  );
}

export default Map;
