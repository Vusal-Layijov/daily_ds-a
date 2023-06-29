function moveZeroes(nums) {
    // Create a pointer called `firstZero` that points to the left-most
    // zero n the array.
    let firstZero = -1;
    // Starts as -1 because there are no zeroes encountered yet
    debugger
    // Iterate through the array.
    for (let i = 0; i < nums.length; i++) {
        // If `firstZero` has not been set, continue on until you reach a zero
        if (firstZero === -1) {

            // When you reach the first zero, set `firstZero` to the current index
            if (nums[i] === 0) firstZero = i;
        }

        // When you reach a non-zero value
        else if (nums[i] !== 0) {
            // swap it's position with `firstZero`
            [nums[i], nums[firstZero]] = [nums[firstZero], nums[i]];
            // and increment `firstZero`
            firstZero++;
        }
    }
    debugger
    return nums;
}
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1];

function oddEvenCompare(a, b) {
    if (a % 2 === 1 && b % 2 === 0) return 1;
     if (a % 2 === 0 && b % 2 === 1) return -1;
    return -1;
}