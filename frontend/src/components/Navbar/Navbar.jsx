import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import './Navbar.css';

function Navbar() {
    const handleRefreshChartData = () => {
        axios.post("http://127.0.0.1:5000/updatecharts")
            .then((response) => {
            console.log(response.data.message);
            // Handle success, e.g., show a success message to the user
            })
            .catch((error) => {
            console.error(error);
            // Handle error, e.g., show an error message to the user
            });
    };

    return (
        <nav className="navbar">
            <ul>
                {/* 
                TODO: 
                - turn the href hashtags into actual urls e.g. /streaming 
                - add more options to navbar
                */}
                <li><a href="/">Home</a></li>
                <li><a href="#">Streaming</a></li>
                <li><Link to="/officialcharts">Official Charts</Link></li>
                <li><button className="button" onClick={handleRefreshChartData}>Refresh Chart Data</button></li>
            </ul>
        </nav>
    )
}

export default Navbar;
