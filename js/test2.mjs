import fetch from 'node-fetch';

async function getTopicCount(topic) {
    try {
        // Encode the topic to handle spaces and special characters in the URL
        const encodedTopic = encodeURIComponent(topic);

        // Construct the URL with the encoded topic
        const url = `https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=${encodedTopic}`;

        // Perform the fetch operation
        const response = await fetch(url);

        // Parse the JSON response
        const data = await response.json();
        const count = countPizzaOccurrences(data)
        return count

        // Output the fetched data

    } catch (error) {
        // Handle any errors that occur during the fetch operation
        console.error('Failed to fetch data:', error);
    }
}
function countPizzaOccurrences(data) {
    // Extract the text content from the object
    const textContent = data.parse.text['*'];

    // Convert the text to lower case to make the search case-insensitive
    const lowerCaseText = textContent.toLowerCase();

    // Use a regular expression to find all occurrences of 'pizza'
    const matches = lowerCaseText.match(/pizza/g); // 'g' flag for global search

    // The number of matches is the number of times 'pizza' appears
    const count = matches ? matches.length : 0;

    return count;
}
console.log(getTopicCount('pizza'))
function solution(a) {

    var indexOfMinimum = -1;
    var minimalSum = Number.MAX_VALUE;

    for (var i = 0; i < a.length; i++) {
        var sum = 0;
        for (var j = 0; j < a.length; j++) {
            sum += Math.abs(a[i] - a[j]);
        }
        if (sum < minimalSum) {
            minimalSum = sum;
            indexOfMinimum = i;
        }
    }

    return a[indexOfMinimum];
}


var maxProduct = function (nums) {
    let res = Math.max(...nums);
    let curMin = 1;
    let curMax = 1;

    for (let n of nums) {
        if (n === 0) {
            curMin = 1;
            curMax = 1;
            continue;
        }

        let tmp = curMax; // Store the original curMax before updating
        curMax = Math.max(curMax * n, curMin * n, n);
        curMin = Math.min(tmp * n, curMin * n, n);

        res = Math.max(curMax, res);
    }
    return res;
};
var minimumDifference = function (nums, k) {
    if (nums.length == 1) {
        return 0
    }
    nums.sort((a, b) => a - b)
    let minS = Infinity
    for (let i = 0; i <= nums.length - k; i++) {
        minS = Math.min(minS, nums[i + k - 1] - nums[i])
    }
    return minS

};
var mergeAlternately = function (word1, word2) {
    let res = '';
    let i = 0;

    // Interleave characters from both strings
    while (i < word1.length || i < word2.length) {
        if (i < word1.length) res += word1[i];
        if (i < word2.length) res += word2[i];
        i++;
    }

    return res;
};
var containsNearbyDuplicate = function (nums, k) {
    let myObj = {}
    for (let i = 0; i < nums.length; i++) {
        if (myObj[nums[i]]) {
            myObj[nums[i]].push(i)
        } else {
            myObj[nums[i]] = [i]
        }
    }
    for (let key in myObj) {
        for (let i = myObj[key].length - 1; i > 0; i--) {
            if (myObj[key][i] - myObj[key][i - 1] <= k) {
                return true
            }
        }
    }
    return false
};
var numOfSubarrays = function (arr, k, threshold) {
    let eS = arr.slice(0, k - 1).reduce((e, acc) => e + acc, 0)
    console.log(eS)
    let res = 0
    for (let i = 0; i < arr.length - k + 1; i++) {
        eS += arr[i + k - 1]
        let av = eS / k
        if (av >= threshold) res += 1
        eS -= arr[i]
    }
    return res
};
var calPoints = function (operations) {
    let records = [];
    console.log(operations);
    for (let o of operations) {
        if (o == '+') {
            records.push(records[records.length - 1] + records[records.length - 2]);
        } else if (o == 'D') {
            records.push(records[records.length - 1] * 2);
        } else if (o == 'C') {
            records.pop();
        } else {
            records.push(parseInt(o));
        }
    }
    return records.reduce((a, e) => a + e, 0);
};
var makeGood = function (s) {
    if (s.length === 0) return '';  // Check if the input string is empty
    let stack = [s[0]];  // Initialize the stack with the first character if not empty
    for (let i = 1; i < s.length; i++) {
        if (stack.length > 0 && stack[stack.length - 1].toLowerCase() === s[i].toLowerCase() && stack[stack.length - 1] !== s[i]) {
            stack.pop();  // Pop if characters are same letter different case
        } else {
            stack.push(s[i]);  // Otherwise, push the current character
        }
    }
    return stack.join('');  // Join the stack to form the resultant string
};
