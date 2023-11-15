#!/usr/bin/node

exports.logMe = (function () {
  let narg = 0;

  return function (item) {
    console.log(narg + ': ' + item);
    narg++;
  };
})();
