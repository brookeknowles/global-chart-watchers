# Global Chart Watchers

This website lets you easily compare the biggest songs around the world on the official singles charts and the biggest streaming platforms (Spotify, Apple Music, YouTube). 

Simply click on a country to see the top 3 songs from each platform, or just hover over a country to see the #1 single on the official singles charts. To see the entire official singles chart, click on the 'Full Charts' button. Use the 'Refresh Chart Data' button to update the website with the most up-to-date data. 

![gcw-example](https://github.com/brookeknowles/global-chart-watchers/assets/62309663/f9d7aaeb-46d9-4996-bdb2-c456c6d61da1)


Currently supported countries: 
- Australia
- Canada
- France
- Ireland
- New Zealand
- UK
- USA

---- 
## 🌐 Frontend
The frontend was created using React JS. 

To run frontend:
- Navigate to frontend directory: `cd frontend`
- Install dependencies: `npm install`
- Start frontend: `npm start`
- Navigate to `localhost:3000` in your favourite web browser
---

## 💻 Backend
The backend is created using Python/Flask

To run backend:
- Install conda environment: `conda create -n <environment-name> --file req.txt`
- Activate the environment: `conda activate <environment-name>`
- Navigate to backend directory: `cd backend`
- Start python server: `python app.py`
- The server will be running on `localhost:5000`

When clicking on the 'refresh chart data' button in the frontend, the `/updatecharts` endpoint is called, which fetches the chart and streaming data from each of the supported countries (via web scraping with Beautiful Soup) and stores it in the database. It then saves the data to the `/numberones`, `/officialcharts/{country}`, `/spotify/{country}`, `/applemusic/{country}`, `/youtube/{country}`, and `/countrypopup/{country}` endpoints for easy retrieval from the frontend. 

### Database
The database used in this project is a Firebase firestore NoSQL database. To use this app you will need to create a Firebase account and install the admin SDK ([read the docs](https://firebase.google.com/docs/firestore/quickstart) for more info/instructions on this). After that's all set up, just replace line 10 of `backend/firebase_utils.py` with the path to your sdk: `cred = credentials.Certificate(path_to_sdk.json)`, and everything should be sweet to go from there!

---
## 🚧 Roadmap
More countries will be added in due time, and I will likely add different streaming services in the markets where Spotify/AM/YT doesn't dominate as hard too. If you're reading this and interested, feel free to make a pull request to add any new countries. 

Note that the chart data is retrieved through web scraping, so will only work as long as the websites I'm scraping from do not change their HTML structure 😅
