def is_valid(s):
    # Create a dictionary to count character frequencies
    char_count = {}

    # Count the frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Create a dictionary to count frequencies of frequencies
    freq_count = {}

    # Count the frequency of frequencies
    for count in char_count.values():
        if count in freq_count:
            freq_count[count] += 1
        else:
            freq_count[count] = 1

    # If there is only one unique frequency, the string is valid
    if len(freq_count) == 1:
        return "YES"

    # If there are two unique frequencies and one of them is 1, the string is valid
    if len(freq_count) == 2:
        freq1, freq2 = freq_count.keys()
        count1, count2 = freq_count.values()
        if (count1 == 1 and (freq1 - freq2 == 1 or freq1 == 1)) or (count2 == 1 and (freq2 - freq1 == 1 or freq2 == 1)):
            return "YES"

    # Otherwise, the string is not valid
    return "NO"
