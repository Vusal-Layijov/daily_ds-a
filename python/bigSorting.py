def bigSorting(unsorted):

    unsorted.sort(key = lambda x: int(x))

    return unsorted


def number_of_points(nums):
    # Write your code here
    myset = set()
    for pair in nums:
        for num in range(pair[0], pair[1]+1):
            myset.add(num)
    print(myset)
    return len(myset)
