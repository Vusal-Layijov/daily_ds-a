function equalStacks(h1, h2, h3) {
    // Calculate the cumulative heights of each stack
    let sum1 = h1.reduce((acc, val) => acc + val, 0);
    let sum2 = h2.reduce((acc, val) => acc + val, 0);
    let sum3 = h3.reduce((acc, val) => acc + val, 0);

    while (true) {
        // Find the minimum cumulative height among the three stacks
        let minSum = Math.min(sum1, sum2, sum3);

        // If any of the stacks is empty, return 0 (no common height)
        if (minSum === 0) {
            return 0;
        }

        // Check if the top element of stack 1 can be removed to equalize heights
        while (sum1 > minSum) {
            sum1 -= h1.shift();
        }

        // Check if the top element of stack 2 can be removed to equalize heights
        while (sum2 > minSum) {
            sum2 -= h2.shift();
        }

        // Check if the top element of stack 3 can be removed to equalize heights
        while (sum3 > minSum) {
            sum3 -= h3.shift();
        }

        // If all stacks are equal in height, return the common height
        if (sum1 === sum2 && sum1 === sum3) {
            return sum1;
        }
    }
}