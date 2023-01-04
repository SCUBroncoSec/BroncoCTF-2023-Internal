//Imports
const express = require("express")
const svgCaptcha = require('svg-captcha');
const session = require("express-session")
const fs = require("fs");

//Create express server
const server = express();
const PORT = process.env.PORT || 3000;

//Serve static HTML
server.use(express.static('public'));

//Listen on $PORT
server.listen(PORT, () => console.log(`Web server listening on port: ${PORT}`));