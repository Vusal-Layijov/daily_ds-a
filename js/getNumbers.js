async function getPhoneNumbers(country, phoneNumber) {
    let data = await getCountryData(country)

    if (data.data.length < 1) return '-1'
    let code = Math.max(data.data[0].callingCodes)
    return `+${code} ${phoneNumber}`
}
async function getCountryData(countryName) {
    const url = `https://jsonmock.hackerrank.com/api/countries?name=${countryName}`;

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching country data:', error);
    }
}
var maxSubArray = function (nums) {
    let maxSub = nums[0]
    let curSum = 0
    for (let n of nums) {
        if (curSum < 0) {
            curSum = 0
        }
        curSum += n
        maxSub = Math.max(maxSub, curSum)

    }
    return maxSub

};