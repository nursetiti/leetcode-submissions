var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const existed =
        this.cache.has(key) && this.cache.get(key).expiresAt > now;

    this.cache.set(key, {
        value: value,
        expiresAt: now + duration
    });

    return existed;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();

    if (!this.cache.has(key)) return -1;

    const entry = this.cache.get(key);
    if (entry.expiresAt <= now) {
        this.cache.delete(key);
        return -1;
    }

    return entry.value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (const [key, entry] of this.cache) {
        if (entry.expiresAt > now) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }

    return count;
};
