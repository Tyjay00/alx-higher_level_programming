# Node.js Scripts

This repository contains several Node.js scripts that interact with APIs and the file system.

## Dependencies

All scripts require Node.js and the `request` module. You can install `request` using npm (Node Package Manager) by running `npm install request` in your terminal.

## Scripts

### Script 1: Fetch Film Title from SWAPI

This script fetches data from the Star Wars API (SWAPI) and logs the title of a specific film.

Usage: `node script1.js <film_id>`

### Script 2: Count Characters in Films

This script fetches data from an API and counts the number of films in which a specific character appears.

Usage: `node script2.js <url>`

### Script 3: Download File

This script downloads a file from a given URL and saves it to a specified location.

Usage: `node script3.js <url> <file_path>`

### Script 4: Count Completed Tasks

This script fetches data from a given URL and logs the number of completed tasks by each user.

Usage: `node script4.js <url>`

### Script 5: Read File

This script reads a file and prints its content to the console.

Usage: `node script5.js <file_path>`

### Script 6: Write to File

This script writes a string to a file.

Usage: `node script6.js <file_path> <string>`

### Script 7: Fetch Character Names from SWAPI

This script fetches data from the SWAPI and prints the names of characters in a specific film.

Usage: `node script7.js <film_id>`

### Script 8: Fetch Character Names from SWAPI (Recursive)

This script fetches data from the SWAPI and prints the names of characters in a specific film. It uses recursion to handle asynchronous requests.

Usage: `node script8.js <film_id>`

## Note

These scripts depend on the availability and the current structure of the APIs. If the APIs are down or if the structure of the data changes, the scripts may not work as expected.
