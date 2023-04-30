# Global Chart Watchers

WIP website to see charts and streaming data from all over the world

---- 
## Frontend
Frontend is created using React JS

to run frontend:
- cd into frontend directory
- `npm start`

---

## Backend
Backend is created using Flask

To run backend:
- `conda activate brooke`
- cd into backend directory
- `python server.py`

#### API routes:
something like ... 
- /officialcharts/{country}
- /streaming/{service}/{country}

---

## TODO/Roadmap
Homepage will have the logo, a nav bar, a map, and a footer

NavBar:
- Streaming site data
    - Spotify
    - Youtube
    - Melon
    - Ganaa
    - others...
- world charts (i.e. what the map will show)
- artists (select an artist, see their streaming data, chart data, maybe a map or graph showing their global popularity or trends)
- songs (same as above but for a particular song (or album))

Map:
- click on each country to see their singles charts (add album charts later)