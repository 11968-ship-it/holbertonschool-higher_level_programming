#!/usr/bin/node
const args = process.argv.slice(2).map(n => parseInt(n));

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
