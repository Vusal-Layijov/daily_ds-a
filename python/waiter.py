def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(q):
    primes = []
    num = 2
    while len(primes) < q:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def waiter(number, q):
    answers = []
    stack_a = number
    primes = generate_primes(q)

    for i in range(q):
        stack_b = []
        new_stack_a = []

        while stack_a:
            plate = stack_a.pop()
            if plate % primes[i] == 0:
                stack_b.append(plate)
            else:
                new_stack_a.append(plate)

        answers.extend(reversed(stack_b))
        stack_a = new_stack_a

    answers.extend(reversed(stack_a))
    return answers