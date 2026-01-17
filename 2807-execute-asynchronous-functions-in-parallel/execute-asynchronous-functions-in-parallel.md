<h2><a href="https://leetcode.com/problems/execute-asynchronous-functions-in-parallel">Execute Asynchronous Functions in Parallel</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an array of&nbsp;asynchronous functions&nbsp;<code>functions</code>, return a new promise <code>promise</code>. Each function in the array accepts no arguments&nbsp;and returns a promise. All the promises should be executed in parallel.</p>

<p><code>promise</code> resolves:</p>

<ul>
	<li>When all the promises returned from&nbsp;<code>functions</code>&nbsp;were resolved successfully in parallel.&nbsp;The resolved&nbsp;value of&nbsp;<code>promise</code> should be an array of all the resolved values of promises in the same order as they were in the&nbsp;<code>functions</code>. The <code>promise</code> should resolve when all the asynchronous functions in the array have completed execution in parallel.</li>
</ul>

<p><code>promise</code> rejects:</p>

<ul>
	<li>When any&nbsp;of the promises&nbsp;returned from&nbsp;<code>functions</code>&nbsp;were rejected.&nbsp;<code>promise</code> should also&nbsp;reject&nbsp;with the reason of the first rejection.</li>
</ul>

<p>Please solve it without using the built-in&nbsp;<code>Promise.all</code>&nbsp;function.</p>

# Approach
Since the idea was to resolve the promise only if the promises from the array of functions were ALL resolved successfully, I had a resolved promise counter.After all the promises from the array of functions were resolved/reject, i compared the promiseCounter to my initial function length and only resolved my output if they are equal.

# Complexities
- Time Complexity: 0(n)
- Space Complexity: 0(n)

