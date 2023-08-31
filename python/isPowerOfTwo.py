def is_power_of_two(x):
    return (x & (x - 1)) == 0


def counterGame(n):
    louise_turn = True

    while n > 1:
        if is_power_of_two(n):
            n //= 2
        else:
            largest_power_of_two = 1 << (n.bit_length() - 1)
            n -= largest_power_of_two

        louise_turn = not louise_turn

    return "Louise" if louise_turn else "Richard"
