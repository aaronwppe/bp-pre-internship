const express = require("express");
const logger = require("./middleware/logger");
const { notFoundHandler, internalErrorHandler } = require("./middleware/error_handlers");

const port = 3000;
const app = express();

// middlewares
app.use(express.static("public"));  // allow GET /post-data.html
app.use(express.urlencoded({ extended: false }));   // to read POST json body
app.use(logger);

app.get('/', (req, res) => {
    return res.status(200)
        .send("Welcome to Express!");
});

app.post('/data', (req, res) => {
    console.log("Received data:");
    console.log(req.body);

    return res.status(200)
        .send("Data Received.");
});

app.get('/users', (req, res) => {
    const data = [
        "user 1",
        "user 2",
        "user 3",
    ];

    return res.status(200)
        .json({
            success: true,
            users: data,
        });
});

app.get('/external-posts', async (req, res) => {
    const url = "https://jsonplaceholder.typicode.com/posts";
    const response = await fetch(url);
    const data = await response.json();

    res.status(200)
        .json({
            success: true,
            posts: data,
        });
});

// error handling middlewares
app.use(notFoundHandler);
app.use(internalErrorHandler);

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});