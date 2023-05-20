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
- `conda activate global-chart-watchers`
- cd into backend directory
- `python app.py`

Database is firebase/cloud firestore

#### API routes:
- GET /numberones
    - retrieves data of #1 song and artist for each supported country
- POST /updatecharts 
    - updates the database with current chart information
- GET /officialcharts/{country}
    - retreives official weekly singles chart for a specified country
- GET /spotify/{country}
    - retreives daily spotify chart for a specified country
- GET /applemusic/{country}
    - retreives weekly apple music chart for a specified country
- GET /youtube/{country}
    - retreives weekly youtube chart for a specified country
- GET /countrypopup/{country}
    - retreives the data to show on the popups 
---

## TODO

- Other/less common streaming site data
    - Melon
    - Ganaa
    - others...

- artists (select an artist, see their streaming data, chart data, maybe a map or graph showing their global popularity or trends)
- songs (same as above but for a particular song (or album))
- inverse points list, where i rank the top 100 least popular (by all time points) 'hits' to hit #1 on BB

Map:
- click on several countries to see a breakdown comparison
