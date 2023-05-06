import React, { useEffect, useRef, useState } from "react";
import "./Map.css";
import jsVectorMap from "jsvectormap";
import "jsvectormap/dist/maps/world-merc.js";

function Map() {
  const mapRef = useRef(null);
  const map = useRef(null);
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    const fetchChartData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/officialcharts/nz");
        const data = await response.json();
        if (Array.isArray(data) && data.length > 0) {
          setChartData(data[0]);
        }
      } catch (error) {
        console.error("Error fetching chart data:", error);
      }
    };

    fetchChartData();
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
      
        if (chartData && code === "NZ") {
          tooltipContent += `<p class="text-xs">Artist: ${chartData.Artist}</p>`;
          tooltipContent += `<p class="text-xs">Position: ${chartData.Position}</p>`;
          tooltipContent += `<p class="text-xs">Track: ${chartData.Track}</p>`;
        }
      
        tooltip.text(tooltipContent, true); // Update tooltip content with HTML
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

  return (
    <div className="map-container">
      <div className="jvm-container" ref={mapRef} />
    </div>
  );
}

export default Map;
