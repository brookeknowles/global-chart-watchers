import React from "react";
import './Navbar.css';

function Navbar() {
    return (
        <nav className="navbar">
            <ul>
                {/* 
                TODO: 
                - turn the href hashtags into actual urls e.g. /streaming 
                - add more options to navbar
                */}
                <li><a href="#">Home</a></li>
                <li><a href="#">Streaming</a></li>
                <li><a href="#">Official Charts</a></li>
                <li><a href="#">Artists</a></li>
            </ul>
        </nav>
    )
}

export default Navbar;