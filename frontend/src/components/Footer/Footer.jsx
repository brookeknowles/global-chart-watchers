import React from "react";
import "./Footer.css"

function Footer() {
    const currentDate = new Date().toLocaleDateString();

    return (
        <div className="footer">
            <p>Last edited: {currentDate}</p>
        </div>
    );
}

export default Footer;
