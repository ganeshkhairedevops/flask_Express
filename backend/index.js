const express = require('express');
const cors = require('cors');
const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

app.post('/api/data', (req, res) => {
    const data = req.body;
    console.log('Received:', data);
    res.json({ message: 'Data received', received: data });
});

app.listen(port, () => {
    console.log(`Express server running at http://localhost:${port}`);
});
