const http = require('http');

const port = 3000;

// create a server instance
const server = http.createServer();

// listener for "request" event
server.on("request", (req, res) => {
    res.writeHead(200, { "content-type": "text/html" });
    res.write("<h1>Welcome to Node.js!</h1>");
    res.end();
});

// configure the port
server.listen(port);

// demo helper module
const helper = require('./helper')
console.log(helper.getMessage());