import React, { useEffect, useState } from 'react'
import './CountryPopup.css'
import { Spotify, Youtube } from '@styled-icons/boxicons-logos'
import { Applemusic } from '@styled-icons/simple-icons'
import ReactCountryFlag from 'react-country-flag'
import countryCodes from './countryCodes.js'
import { fetchData } from './popupData.js'
import { supportedCountries } from './supportedCountries.js'

function CountryPopup({ countryCode, onClose }) {
    const [isSupported, setIsSupported] = useState(true)
    const [data, setData] = useState(null)

    useEffect(() => {
        const fetchCountryData = async () => {
            // Check if the country is supported
            if (!supportedCountries.includes(countryCode)) {
                setIsSupported(false)
            } else {
                setIsSupported(true) // Set to true before fetching data
                const jsonData = await fetchData(countryCode)
                setData(jsonData)
            }
        }

        fetchCountryData()
    }, [countryCode])

    useEffect(() => {
        // Reset data when country is not supported
        if (!isSupported) {
            setData(null)
        }
    }, [isSupported])

    if (!isSupported) {
        return (
            <div className="country-popup">
                <div className="popup-header">
                    <h1 className="country-name">
                        {countryCodes[countryCode]}
                    </h1>
                    <button className="close-button" onClick={onClose}>
                        X
                    </button>
                </div>
                <p>This country is not supported yet.</p>
            </div>
        )
    }

    if (!data) {
        return (
            <div className="country-popup">
                <div className="popup-header">
                    <h1 className="country-name">
                        {countryCodes[countryCode]}
                    </h1>
                    <button className="close-button" onClick={onClose}>
                        X
                    </button>
                </div>
                <p>Loading data...</p>
            </div>
        )
    }

    const { apple_music, official, spotify, youtube } = data

    return (
        <div className="country-popup">
            <div className="popup-header">
                <h1 className="country-name">{countryCodes[countryCode]}</h1>
                <button className="close-button" onClick={onClose}>
                    X
                </button>
            </div>
            <hr className="line" />
            <div className="official-chart-container">
                <h2 className="official-chart-title">Official Chart</h2>
                <hr className="line" />
                <div className="official-top3-container">
                    <ReactCountryFlag
                        countryCode={countryCode}
                        svg
                        style={{
                            width: '2em',
                            height: '2em',
                        }}
                        className="flag-icon"
                    />
                    <ol type="1">
                        {official.map((item) => (
                            <li
                                key={item.Position}
                            >{`${item.Artist} - ${item.Track}`}</li>
                        ))}
                    </ol>
                </div>
            </div>
            <hr className="line" />
            <div className="streaming-container">
                <h2 className="streaming-title">Streaming</h2>
                <hr className="line" />
                <div className="spotify-container">
                    <Spotify className="spotify-icon" />
                    <ol type="1">
                        {spotify.map((item) => (
                            <li
                                key={item.Position}
                            >{`${item.Artist} - ${item.Track}`}</li>
                        ))}
                    </ol>
                </div>
                <hr className="line" />
                <div className="apple-music-container">
                    <Applemusic className="apple-icon" />
                    <ol type="1">
                        {apple_music.map((item) => (
                            <li
                                key={item.Position}
                            >{`${item.Artist} - ${item.Track}`}</li>
                        ))}
                    </ol>
                </div>
                <hr className="line" />
                <div className="youtube-container">
                    <Youtube className="youtube-icon" />
                    <ol type="1">
                        {youtube.map((item) => (
                            <li
                                key={item.Position}
                            >{`${item.Artist} - ${item.Track}`}</li>
                        ))}
                    </ol>
                </div>
                <hr className="line" />
            </div>
        </div>
    )
}

export default CountryPopup
