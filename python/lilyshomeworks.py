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


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        finish = len(height)-1
        maxArea = 0
        while start < finish:
            width = finish-start
            h = min(height[start], height[finish])
            maxArea = max(maxArea, h * width)
            if height[start] < height[finish]:
                start += 1
            else:
                finish -= 1

        return maxArea
