var reverseWords = function (s) {
    let newA = s.split(' ')
    newA.reverse()
    console.log(newA)
    let son = newA.filter(word => word)
    console.log('ssss', son)
    return son.join(' ')
};