#!/usr/bin/node
// reads a file and prints its content
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
