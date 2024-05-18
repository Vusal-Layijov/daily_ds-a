var compactObject = function (obj) {
    if (obj === null) return null
    if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject)
    if (typeof obj !== "object") return obj;
    const compacted = {}
    for (let key in obj) {
        let value = compactObject(obj[key])
        if (Boolean(value)) compacted[key] = value
    }
    return compacted
};
var canJump = function (nums) {
    let goal = nums.length - 1
    for (let i = nums.length - 1; i--; i >= 0) {
        if (i + nums[i] >= goal) {
            goal = i
        }
    }
    let togo;
    goal === 0 ? togo = true : togo = false
    return togo
};