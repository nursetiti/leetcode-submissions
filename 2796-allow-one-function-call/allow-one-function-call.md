<h2><a href="https://leetcode.com/problems/allow-one-function-call">Allow One Function Call</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given a function <code>fn</code>, return a new function that is identical to the original function except that it ensures&nbsp;<code>fn</code>&nbsp;is&nbsp;called at most once.</p>

<ul>
	<li>The first time the returned function is called, it should return the same result as&nbsp;<code>fn</code>.</li>
	<li>Every subsequent time it is called, it should return&nbsp;<code>undefined</code>.</li>
</ul>

# Approach
I needed some kind of state between the two functions where only one state can trigger an If statement.My initial state was set to false so I called an if statement which is valid if my state is false, in the if statement, after our function is passed over our args array for the first time, our state is set to true so that the subsequent times our function is called again, the if statement won't hold for it and we would return our default output: undefined .

# Complexities
- Time Complexity - 0(n)
- Space Complexity - 0(1)
