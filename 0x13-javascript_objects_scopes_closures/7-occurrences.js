#!/usr/bin/node
//function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  list.forEach(function (item) {
    if (item === searchElement) {
      c++;
    }
  });
  return c;
}
