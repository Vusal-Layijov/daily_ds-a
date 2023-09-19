function truckTour(petrolPumps) {
    // Write your code here
    let totalPetrol = 0; // Total petrol available
    let currentPetrol = 0; // Petrol at current pump
    let startingPump = 0; // Starting petrol pump index

    for (let i = 0; i < petrolPumps.length; i++) {
        const [petrol, distance] = petrolPumps[i];
        totalPetrol += petrol - distance;
        currentPetrol += petrol - distance;

        if (currentPetrol < 0 || totalPetrol < 0) {
            // If the current petrol is negative, reset and start from the next pump
            currentPetrol = 0;
            startingPump = i + 1;
            totalPetrol = 0
        }
    }

    // If total petrol is greater than or equal to total distance, a solution exists.
    if (totalPetrol >= 0) {
        return startingPump;
    }

    return -1; // If no solution exists
}