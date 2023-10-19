def makeSwaps(arr):
    # sort list of values while keeping their original index
    beautiful_arr = (sorted(list(enumerate(arr)), key=lambda x: x[1]))
    num_swaps = 0
    for idx in range(len(arr)):
        while True:
            # while the original won't correspond to the "correct" by order index, swap
            if beautiful_arr[idx][0] == idx:
                break
            else:
                num_swaps += 1
                swapped_idx = beautiful_arr[idx][0]
                beautiful_arr[idx], beautiful_arr[swapped_idx] = beautiful_arr[swapped_idx], beautiful_arr[idx]

    return num_swaps


def lilysHomework(arr):
    return min(makeSwaps(arr), makeSwaps(arr[::-1]))
