function noPrefix(words) {
    let prefixes = new Set();
    let prevWords = new Set();
    for (let w of words) {
        // Check if w is prefix of any previous word
        if (prefixes.has(w)) {
            console.log(`BAD SET \n${w}`);
            return;
        }
        // Check if any previous word is a prefix of w
        for (let i = 1; i <= w.length; i++) {
            if (prevWords.has(w.substring(0, i))) {
                console.log(`BAD SET \n${w}`);
                return;
            }
            prefixes.add(w.substring(0, i));
        }
        prevWords.add(w);
    }
    console.log("GOOD SET");
}

var rob = function (nums) {
    let rob1 = 0
    let rob2 = 0

    for (let r of nums) {
        tmp = rob1 + r
        rob1 = rob2
        rob2 = Math.max(tmp, rob1)
    }

    return rob2
};