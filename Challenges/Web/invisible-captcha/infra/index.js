//Imports
const express = require("express")
const svgCaptcha = require('svg-captcha');
const session = require("express-session")

//Create express server
const server = express();
const PORT = process.env.PORT || 8080;

//Serve static HTML
server.use(express.static('public'));

//Enable session middleware
server.use(session({
    secret: "abc123",
    saveUninitialized: true,
    cookie: {maxAge: 30 * 60 * 1000}, // 30 Minutes
    resave: false
}));

//Generate and send captcha
server.get('/generateCaptcha', (req, res) =>
{
    let captcha = svgCaptcha.create();
    req.session.captcha = captcha.text;

    res.type('svg');
    res.status(200).send(captcha.data);
});

//Listen on $PORT
server.listen(PORT, () => console.log(`Web server listening on port: ${PORT}`));