#!/usr/bin/node
//searches the second biggest integer in the list of arguments.
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = [];
  for (let i = 2; i < process.argv.length; i++) {
    args[i - 2] = process.argv[i];
  }
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
