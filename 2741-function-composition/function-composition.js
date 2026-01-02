/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {

    return function(x) {
        //starting with x
        let finalAnswer = x;

        //iterate through the functions(in reverse order)
        for(let i=functions.length-1; i>=0; i--){
            finalAnswer = functions[i](finalAnswer) 
        }
        return finalAnswer;
    }
    
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */