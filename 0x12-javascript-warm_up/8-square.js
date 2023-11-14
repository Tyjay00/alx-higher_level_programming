#!/usr/bin/node

const size = process.argv[2];

if (size === undefined || isNaN(size)) {
  console.log('Missing size');
} else {
  const x = Number(size);

  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
