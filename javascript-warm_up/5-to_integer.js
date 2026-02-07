#!/usr/bin/node
const A = process.argv[2];
const N = parseInt(A);
if (isNaN(N)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + N);
}
