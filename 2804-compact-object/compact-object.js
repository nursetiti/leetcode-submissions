/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
    if (!obj) return obj;

    if (Array.isArray(obj)) {
        const res = [];
        for (let value of obj) {
            const compacted = compactObject(value);
            if (Boolean(compacted)) {
                res.push(compacted);
            }
        }
        return res;
    }

    if (typeof obj === "object") {
        const res = {};
        for (let key in obj) {
            const compacted = compactObject(obj[key]);
            if (Boolean(compacted)) {
                res[key] = compacted;
            }
        }
        return res;
    }

    return obj;
};
