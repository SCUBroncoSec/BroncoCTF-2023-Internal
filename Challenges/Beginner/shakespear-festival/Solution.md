# Solution

1. Running the `nc` command with provided IP and port numbers (i.e. `nc 127.0.0.1 8080`) will start printing "Empire Striketh Back" to the console.
2. Every 10-20 seconds, the flag will be randomly inserted into the text appearing in the console.
3. To solve, the user need just wait until they see the flag.
4. (Optional) To make it sligtly easier, the user could pipe the output into a grep command to search for lines containing the flag format (i.e. `nc 127.0.0.1 8080 | grep 'broncoctf{'`). This will make it easier to identify when the flag is printed.