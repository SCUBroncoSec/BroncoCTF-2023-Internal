//Imports
const express = require("express")
const svgCaptcha = require('svg-captcha');
const session = require("express-session")
const fs = require("fs");

let flag = "There seems to be no flag loaded. If you see this message please contact an admin!"

//Read flag from text file
try {
    flag = fs.readFileSync('./flag.txt', 'utf-8');
} catch (error) {
    console.error(`Error reading flag.txt:\n${error}`);
}

//Create express server
const server = express();
const PORT = process.env.PORT || 3000;

//Serve static HTML
server.use(express.static('static'));

//Enable session middleware
server.use(session({
    secret: "abc123",
    saveUninitialized: true,
    cookie: {maxAge: 30 * 60 * 1000}, // 30 Minutes
    resave: false
}));

//Parse form data
server.use(express.urlencoded({ extended: true }));

//Generate and send captcha
server.get('/generateCaptcha', (req, res) =>
{
    let captcha = svgCaptcha.create();
    req.session.captcha = captcha.text;

    res.type('svg');
    res.status(200).send(captcha.data);
});

//Validate captcha
server.post('/validateCaptcha', (req, res) => {
    if (req.body.captcha == req.session.captcha) {
        res.status(200).send(flag)
    } else {
        res.status(200).send("Incorrect Captcha")
    }
});

//Listen on $PORT
server.listen(PORT, () => console.log(`Web server listening on port: ${PORT}`));