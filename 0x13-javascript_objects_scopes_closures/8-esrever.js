#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const newlist = [];
  for (let i = 0; i < list.length; i++) {
    newlist.push(list[list.length - i - 1]);
  }
  return newlist;
};
