<h2><a href="https://leetcode.com/problems/chunk-array">Chunk Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array <code>arr</code> and a chunk size <code>size</code>, return a <strong>chunked</strong> array.</p>

<p>A <strong>chunked</strong> array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.</p>

<p>Please solve it without using lodash&#39;s <code>_.chunk</code> function.</p>

# Approach
I looped through the given array from the beginning and at every interval of the size specified. I then used the slice method to create a sub array from our current index up until the amount specified by our size. The new chunk is then pushed into the array.

# Complexities:
- Time Complexity - 0(n)
- Space Complexity-0(n)
