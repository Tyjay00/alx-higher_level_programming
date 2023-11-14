#!/usr/bin/node

const occurrences = process.argv[2];

if (occurrences === undefined || isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  const count = Number(occurrences);

  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
