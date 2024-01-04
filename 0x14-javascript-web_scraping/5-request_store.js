#!/usr/bin/node
//This is a Node.js script that downloads a file from a given URL and saves it to a specified location.

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
