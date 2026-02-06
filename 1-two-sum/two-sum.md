<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

# Approach
To solve the Two Sum problem efficiently, I use a dictionary to store numbers I have already seen along with their indices so that I can quickly check whether a matching number has appeared earlier.
I then iterate through the list once. For each element num at index i, I calculate the value needed to reach the target:
needed=target−num
Before storing the current number, I check whether this required value already exists in the hash map. If it exists, it means I previously encountered the number that pairs with the current element to produce the target sum, so I immediately return the indices of the pair.
If the complement is not found, I store the current number and its index in the hash map and continue the iteration until the matching pair is found.

# Complexities
- Time Complexity : 0(n)
- Space Complexity : 0(n)
