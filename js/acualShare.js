function bonAppetit(bill, k, b) {
    let total = 0;

    for (let i = 0; i < bill.length; i++) {
        if (k != i) {
            total += bill[i];
        }
    }

    let actualShare = total / 2;

    if (b == actualShare) {
        console.log("Bon Appetit")
    } else {
        console.log(b - actualShare)
    }
}
function sockMerchant(n, ar) {
    // Write your code here
    let obj = {}
    let res = 0
    for (let s of ar) {
        if (s in obj) {
            obj[s] += 1
            if (obj[s] == 2) {
                res += 1
                obj[s] = 0
            }

        } else {
            obj[s] = 1
        }
    }
    return res
}
function icecreamParlor(m, arr) {
    for (let i = 0; i < arr.length; i++) {
        let balance = m - arr[i];
        let find = arr.findIndex((num, index) => {
            return i != index && num === balance
        })
        if (find != -1) {
            return [i + 1, find + 1]
        }
    }
}
const largestComponenet = (graph) =>{
    let longest=0
    let visited= new Set()
    for (let node in graph){
        let size = explore(graph,node,visited)
        if(size>longest)longest=size
    }
}
const explore = (graph,node,visited)=>{
    if (visited.has(node)) return 0
    let size=1
    visited.add(size)
    for (let neigh of graph[node]){
        size+= explore(graph,neigh,visited)
    }
    return size

}
export function monthlyCharge(yearMonth, subscription, users) {
    if (!subscription) return 0; // Step 1

    // Parse year and month for comparison
    const [year, month] = yearMonth.split("-").map(Number);
    const firstDayOfMonth = new Date(year, month - 1, 1);
    const lastDayOfMonth = new Date(year, month, 0); // Day 0 of the next month gives the last day of the current month

    let totalCharge = 0;

    users.forEach(user => {
        const activatedOn = user.activatedOn;
        const deactivatedOn = user.deactivatedOn || new Date(); // Treat null as not yet deactivated

        // Check if the user was active during the specified month
        if ((activatedOn <= lastDayOfMonth && (!user.deactivatedOn || deactivatedOn >= firstDayOfMonth))) {
            totalCharge += subscription.monthlyPriceInCents;
        }
    });

    return totalCharge; // Step 5
}

// maxArea
var maxArea = function (height) {
    let maxWater = 0
    let i = 0
    while (i < height.length - 1) {
        for (let j = i + 1; j < height.length; j++) {
            maxWater = Math.max(maxWater, ((j - i) * Math.min(height[i], height[j])))
        }
        i++
    }
    return maxWater
};

async function getMovieList(year) {
    let togo = []
    try {
        const response = await fetch(`https://jsonmock.hackerrank.com/api/moviesdata?Year=${year}`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Data fetched successfully');
        for (let m of data.data) {
            togo.push(m.Title)
        }
        return togo; 
    } catch (error) {
        console.error('Failed to fetch data:', error);
    }
}
function biggerIsGreater(w) {
    let arr = w.split('');
    let i = arr.length - 2;

    // Step 1: Find pivot
    while (i >= 0 && arr[i] >= arr[i + 1]) {
        i--;
    }

    if (i < 0) return 'no answer';

    // Step 2: Find rightmost successor to the pivot
    let j = arr.length - 1;
    while (arr[j] <= arr[i]) {
        j--;

    }

    // Step 3: Swap pivot and successor
    [arr[i], arr[j]] = [arr[j], arr[i]];

    // Step 4: Reverse the suffix
    let left = i + 1, right = arr.length - 1;
    while (left < right) {
        [arr[left], arr[right]] = [arr[right], arr[left]];
        left++;
        right--;
    }

    return arr.join('');
}