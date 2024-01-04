#!/usr/bin/node
//This is a Node.js script that reads a file and prints its content to the console.

#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
