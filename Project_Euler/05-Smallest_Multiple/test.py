from solution import smallest_multiple

def test_smallest_multiple(n, exp):
    got = smallest_multiple(n)
    if got != exp:
        raise "Failed for n=" + str(n) + "  got=" + str(got) + "  but exp=" + str(exp)

import collections
from operator import mul
from functools import reduce


def prime_factors(num):
    div = 2
    while num > 1:
        if num % div:
            div += 1
            continue
        yield div
        num /= div


def gen_smallest_divisable(divisors):
    factors = collections.defaultdict(int)
    Counter = collections.Counter
    for divisor in divisors:
        div_factors = Counter(prime_factors(divisor))
        for number, amount in div_factors.items():
            factors[number] = max(factors[number], amount)
    return reduce(mul, (n ** a for n, a in factors.items()))

def smallest_multiple_other_dude(multiple):
    return gen_smallest_divisable(range(1, multiple + 1))

if __name__ == "__main__":
    for i in range(1000000, 11000000, 1000):
        print(i)
        smallest_multiple(i)
        #print(i, smallest_multiple(i))
        # input()
        # test_smallest_multiple(i, smallest_multiple_other_dude(i))
