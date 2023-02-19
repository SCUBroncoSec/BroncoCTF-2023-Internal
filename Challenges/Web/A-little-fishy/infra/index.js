const express = require("express")

//Create express server
const server = express();
const PORT = process.env.PORT || 8000;

//Serve static HTML
server.use(express.static('static'))

//Listen on $PORT
server.listen(PORT, () => console.log(`Express listening on port: ${PORT}`));