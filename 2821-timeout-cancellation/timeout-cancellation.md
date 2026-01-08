<h2><a href="https://leetcode.com/problems/timeout-cancellation">Timeout Cancellation</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given a function <code>fn</code>, an array of&nbsp;arguments&nbsp;<code>args</code>, and a timeout&nbsp;<code>t</code>&nbsp;in milliseconds, return a cancel function <code>cancelFn</code>.</p>

<p>After a delay of <code>cancelTimeMs</code>, the returned cancel function <code>cancelFn</code> will be invoked.</p>

# Approach
The idea is to delay running the function using setTimeout and store the returned timeout ID. Then I create a cancel function that calls clearTimeout with that ID so it can stop the function from running if called early. I then returned the cancelFn so it can be invoked later to prevent execution.

# Complexities 
-Time complexity: 0(1)
-Space Complexity: 0(n)
