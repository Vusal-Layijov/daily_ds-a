def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False
    for char in password:
        if char in numbers:
            has_digit = True
        if char in lower_case:
            has_lower = True
        if char in upper_case:
            has_upper = True
        if char in special_characters:
            has_special = True
    toadd = 0
    if not has_digit:
        toadd += 1
    if not has_lower:
        toadd += 1
    if not has_upper:
        toadd += 1
    if not has_special:
        toadd += 1
    if toadd + n < 6:
        toadd += 6-(n+toadd)
    return toadd
