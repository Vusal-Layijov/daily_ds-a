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
