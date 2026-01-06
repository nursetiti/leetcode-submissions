<h2><a href="https://leetcode.com/problems/sleep">Sleep</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given&nbsp;a positive integer <code>millis</code>, write an asynchronous function that sleeps for <code>millis</code>&nbsp;milliseconds. It can resolve any value.</p>

<p><strong>Note</strong> that <em>minor</em> deviation from <code>millis</code> in the actual sleep duration is acceptable.</p>

# Approach
The function returns a promise that gets resolved after certain milliseconds. After the function has gotten resolved,the .then() specified what happens after my function has been resolved, i.e the set ms has passed.

# Complexities
- Time Complexity: 0(1)
- Space Complexity : 0(1)
