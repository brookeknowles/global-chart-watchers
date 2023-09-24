import React from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Header from './components/Header/Header'
import Navbar from './components/Navbar/Navbar'
import Map from './components/Map/Map'
import Footer from './components/Footer/Footer'
import CountryPopup from './components/CountryPopup/CountryPopup'
import OfficialCharts from './components/OfficialChartsPage/OfficialChartsPage'
import './App.css'

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Header />
                <Navbar />
                <Switch>
                    <Route exact path="/" component={Map} />
                    <Route path="/officialcharts" component={OfficialCharts} />
                </Switch>
                <Footer />
            </div>
        </BrowserRouter>
    )
}

export default App
