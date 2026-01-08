<h2><a href="https://leetcode.com/problems/interval-cancellation">Interval Cancellation</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given a function <code>fn</code>, an array of arguments&nbsp;<code>args</code>, and&nbsp;an interval time <code>t</code>, return a cancel function <code>cancelFn</code>.</p>

<p>After a delay of&nbsp;<code>cancelTimeMs</code>, the returned cancel function&nbsp;<code>cancelFn</code>&nbsp;will be invoked.</p>

<pre>
setTimeout(cancelFn, cancelTimeMs)
</pre>

<p>The function <code>fn</code> should be called with <code>args</code> immediately and then called again every&nbsp;<code>t</code> milliseconds&nbsp;until&nbsp;<code>cancelFn</code>&nbsp;is called at <code>cancelTimeMs</code> ms.</p>

# Approach 
The idea was to call the function immediately first, then use setInterval to run it repeatedly every t milliseconds. I store the interval ID returned by setInterval, then created a cancel function that calls clearInterval with that ID to stop further executions.I then return the cancel function so it can be invoked later to stop the repeated calls.

# Complexities
- Time Complexity: O(1)
- Space Complexity: O(1) extra space for the interval ID; O(n) for storing the arguments in the closure.
