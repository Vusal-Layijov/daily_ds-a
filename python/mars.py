def marsExploration(s):
    # Write your code here
    expected = "SOS"
    altered_count = 0

    for i, char in enumerate(s):
        expected_char = expected[i % 3]  # Cycling through "SOS"
        if char != expected_char:
            altered_count += 1

    return altered_count
