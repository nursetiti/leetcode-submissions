/**
 * @param {Function} fn
 * @return {Function}
 */

function memoize(fn) {
  const store = {}; 

  return function (...args) {
   
    const key = String(args);
    if (key in store) {
      return store[key]; 
    }
    //else
    const result = fn(...args); 
    store[key] = result; 
    return result;
  };
}
/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */