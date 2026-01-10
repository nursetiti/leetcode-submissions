<h2><a href="https://leetcode.com/problems/debounce">Debounce</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a function&nbsp;<code>fn</code> and a time in milliseconds&nbsp;<code>t</code>, return&nbsp;a&nbsp;<strong>debounced</strong>&nbsp;version of that function.</p>

<p>A&nbsp;<strong>debounced</strong>&nbsp;function is a function whose execution is delayed by&nbsp;<code>t</code>&nbsp;milliseconds and whose&nbsp;execution is cancelled if it is called again within that window of time. The debounced function should also receive the passed parameters.</p>

<p>For example, let&#39;s say&nbsp;<code>t = 50ms</code>, and the function was called at&nbsp;<code>30ms</code>,&nbsp;<code>60ms</code>, and <code>100ms</code>.</p>

<p>The first 2 function calls would be cancelled, and the 3rd function call would be executed at&nbsp;<code>150ms</code>.</p>

<p>If instead&nbsp;<code>t = 35ms</code>, The 1st call would be cancelled, the 2nd would be executed at&nbsp;<code>95ms</code>, and the 3rd would be executed at&nbsp;<code>135ms</code>.</p>

# Approach
I approached this problem by wrapping the original function in another function that I control. I keep a single timer to track when the function should run. Every time the debounced function is called, I first cancel any existing timer so that previous calls don’t execute. Then I start a new timer to run the original function after the specified delay, passing along the latest arguments. By doing this, I ensure that if the function is called repeatedly in quick succession, only the last call actually runs, and it always uses the most recent input. This makes the function efficient and prevents unnecessary executions while preserving the correct behavior.

# Complexities
- Time Complexity : 0(1)
- Space Complexity : 0(1)
