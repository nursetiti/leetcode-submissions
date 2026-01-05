<h2><a href="https://leetcode.com/problems/memoize">Memoize</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a function <code>fn</code>, return a&nbsp;<strong>memoized</strong>&nbsp;version of that function.</p>

<p>A&nbsp;<strong>memoized&nbsp;</strong>function is a function that will never be called twice with&nbsp;the same inputs. Instead it will return&nbsp;a cached value.</p>

<p>You can assume there are&nbsp;<strong>3&nbsp;</strong>possible input functions:&nbsp;<code>sum</code><strong>, </strong><code>fib</code><strong>,&nbsp;</strong>and&nbsp;<code>factorial</code><strong>.</strong></p>

# Approach
Since the idea is to not call a function twice for the same input, I had to make sure my inputs are stored with a unique key but the key is also dependent on the input value. In my function, I had another function that ran to check every key in my store using the spread operator.the key is gotten by converting the input value to string. If the new key is already in store, it's value is simply returned.If it's not, our funtion is called on the arguments, their value's key is stored and then returned.

# Complexities
-Time Complexity - 
