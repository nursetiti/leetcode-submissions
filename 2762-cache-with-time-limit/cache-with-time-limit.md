<h2><a href="https://leetcode.com/problems/cache-with-time-limit">Cache With Time Limit</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Write a class that allows getting and setting&nbsp;key-value pairs, however a&nbsp;<strong>time until expiration</strong>&nbsp;is associated with each key.</p>

<p>The class has three public methods:</p>

<p><code>set(key, value, duration)</code>:&nbsp;accepts an integer&nbsp;<code>key</code>, an&nbsp;integer&nbsp;<code>value</code>, and a <code>duration</code> in milliseconds. Once the&nbsp;<code>duration</code>&nbsp;has elapsed, the key should be inaccessible. The method should return&nbsp;<code>true</code>&nbsp;if the same&nbsp;un-expired key already exists and <code>false</code> otherwise. Both the value and duration should be overwritten if the key already exists.</p>

<p><code>get(key)</code>: if an un-expired key exists, it should return the associated value. Otherwise it should return&nbsp;<code>-1</code>.</p>

<p><code>count()</code>: returns the count of un-expired keys.</p>

# Approach
Here each key we store isn’t just a key and a value, we also store when it’s supposed to expire. That way, we can check any time if a key is still existing or if it should be ignored.For set, I first check if the key already exists and hasn’t expired yet. If it does, I note that it existed, then I update the key with the new value and a new expiration time.For get, I just check if the key exists and if it hasn’t expired. If it’s expired, I delete it and return -1. Otherwise, I return the value.

# Complexities
- Time Complexity: 0(n) for count,0(1) for set and get
- Space Complexity: 0(n)
