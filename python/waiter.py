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


def journeyToMoon(n, astronaut):
    clusters = [set([i]) for i in range(n)]
    for p in astronaut:
        all_related = clusters[p[0]].union(clusters[p[1]])
        for i in all_related:
            clusters[i] = all_related
    clusters = set([tuple(s) for s in clusters])

    s, s2 = 0, 0
    for c in clusters:
        s += len(c)
        s2 += len(c)**2

    return (s**2-s2)//2


def countingValleys(steps, path):
    # Write your code here
    c1 = 0
    c2 = 0
    for i in path:
        if i == 'D':
            c1 -= 1
        elif i == 'U':
            c1 += 1
        if c1 == 0 and i == 'U':
            c2 += 1
    return c2


#common substring
def commonSubstring(a, b):
    # Write your code here
    res = [False]*len(a)
    for i, word in enumerate(a):
        for letter in word:
            if letter in b[i]:
                res[i] = True
                break
    for r in res:
        print("YES" if r else 'NO')


def getLatestKRequests(requests, K):
    # Write your code here
    mySet = set()
    res = []
    for r in requests[::-1]:
        if K and r not in mySet:
            res.append(r)
            mySet.add(r)
            K-=1
    return res
