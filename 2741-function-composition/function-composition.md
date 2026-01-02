<h2><a href="https://leetcode.com/problems/function-composition">Function Composition</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of functions&nbsp;<code>[f<span style="font-size: 10.8333px;">1</span>, f<sub>2</sub>, f<sub>3</sub>,&nbsp;..., f<sub>n</sub>]</code>, return&nbsp;a new function&nbsp;<code>fn</code>&nbsp;that is the <strong>function&nbsp;composition</strong> of the array of functions.</p>

# Approach
I set my final answer to x so that my finalAnswer will be the identity element if my function array is an empty array.I then iterated through the array of functions backward until we are at the beginning of the array.I applied the current function to my current value of finalAnswer and set the result to finalAnswer. FinalAnswer is returned outside the loop </p>

# Complexities
Time Complexity: 0(n)- Iterating through the array items
