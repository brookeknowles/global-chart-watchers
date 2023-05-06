# Global Chart Watchers

WIP website/hobby project to see charts and streaming data from all over the world.

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
- /officialcharts/{country}
    - currently only NZ is done
---

## TODO/Roadmap

- Streaming site data
    - Spotify
    - Apple music
    - Youtube
    - Melon
    - Ganaa
    - others...
- world charts (i.e. what the map will show)
- artists (select an artist, see their streaming data, chart data, maybe a map or graph showing their global popularity or trends)
- songs (same as above but for a particular song (or album))
- inverse points list, where i rank the top 100 least popular (by all time points) 'hits' to hit #1 on BB

Map:
- hover over a country to see their singles charts (add album charts later)
- click on several countries to see a breakdown comparison

Backend: 
- instead of scraping data when endpoint is hit, maybe have a database that is only updated once a week or something
- Should probs look into legality of web scraping lolz