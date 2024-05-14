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