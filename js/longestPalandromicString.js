var longestPalindrome = function (s) {
    let mysubs= findSub(s)
    let biggest=0
    let biggests=''
    for(let sub of mysubs){
        if(helper(sub) && sub.length>biggest){
            biggest=sub.length
            biggests=sub
        }
    }
    return biggests
};
var helper = function (s) {
    return s === s.split('').reverse().join('')
}
var findSub = function(s){
    let subSet = new Set([s])
    let length = s.length
    for (let i = 0; i< length; i++){
        for (let j=i+1; j<=length;j++){
              subSet.add(s.substring(i,j))  
        }
    }
    return subSet
}