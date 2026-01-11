/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
  if (functions.length === 0) {
    return Promise.resolve([]);
  }

  const outputs = new Array(functions.length);
  let resolvedPromiseCounter = 0;

  return new Promise((resolve, reject) => {
    functions.forEach((promise, index) => {
      promise().then((value) => {
          outputs[index] = value;
          resolvedPromiseCounter += 1;
          if (resolvedPromiseCounter === functions.length) {
            resolve(outputs);
          }
        })
        .catch((err) => {
          reject(err);
        });
    });
  });

};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */