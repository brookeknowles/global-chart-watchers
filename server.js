const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const cors = require('cors');

const app = express();
const port = 3001;

app.use(cors());

// todo fix useless API

app.get('/api/top40', async (req, res) => {
    try {
        const response = await axios.get('https://nztop40.co.nz/chart/singles');
        const $ = cheerio.load(response.data);
        const songs = [];

        $('.chart-table .title').each((i, el) => {
            songs.push({
                rank: i + 1,
                title: $(el).text(),
            });
        });

        res.json(songs);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Failed to fetch top 40 songs' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
