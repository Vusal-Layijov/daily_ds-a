var rob = function (nums) {
    let rob1 = 0
    let rob2 = 0
    for (let num of nums) {
        let tmp = Math.max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = tmp
    }
    return rob2
};
var rob2= function(nums){
   return Math.max(nums[0],rob(nums.slice(1),rob(nums.slice(0,-1))))
}