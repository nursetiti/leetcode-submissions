
# Approach
Here each key we store isn’t just a key and a value, we also store when it’s supposed to expire. That way, we can check any time if a key is still existing or if it should be ignored.For set, I first check if the key already exists and hasn’t expired yet. If it does, I note that it existed, then I update the key with the new value and a new expiration time.For get, I just check if the key exists and if it hasn’t expired. If it’s expired, I delete it and return -1. Otherwise, I return the value.

# Complexities
- Time Complexity: 0(n) for count,0(1) for set and get
- Space Complexity: 0(n)
