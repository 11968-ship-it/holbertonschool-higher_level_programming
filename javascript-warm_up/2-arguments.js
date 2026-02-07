#!/usr/bin/node
const N = process.argv.length - 2;
if (N === 0) {
  console.log('No argument');
} else if (N === 1) {
  console.log('Argument found'); 
} else {
  console.log('Arguments found');
}
