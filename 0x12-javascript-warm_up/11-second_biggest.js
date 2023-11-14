#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numbers = process.argv.slice(2).map(Number);
  const secondLargest = numbers.sort((a, b) => b - a)[1];
  console.log(secondLargest || '0');
}
