#!/usr/bin/node
// Computes and prints a factorial recursively

function factorial (n) {
  if (n === 1) {
	  return (1);
  }

  return (n * factorial(n - 1));
}

if (isNaN(process.argv[2])) {
	console.log('1');
} else {
	console.log(factorial(Number(process.argv[2])));
}
