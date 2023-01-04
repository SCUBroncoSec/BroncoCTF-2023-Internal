# Solution

This is a pretty simple challenge: the captcha isn't rendered, but is still sent to the client.

Open the `Network` tab in the browser devtools. Then request a new captcha. You should see the GET request the browser makes, and the response the API sends (the captcha in SVG form). Some browsers can show the captcha right in the network tab (I know Firefox does this), or you might have to copy the data into a text file and save it as an SVG.
