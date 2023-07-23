def findLowestStartingStair(jumps):
    current_stair = 0
    min_stair = 0

    for jump in jumps:
        current_stair += jump
        min_stair = min(min_stair, current_stair)

    # Calculate the starting stair (lowest_stair)
    starting_stair = 1 - min_stair if min_stair < 0 else 1

    return starting_stair
