#!/bin/python3

from operator import mul

class Option:
    def __init__(self, value, count):
        self.value = value
        self.count = count

n = 5 * 10**5 + 1
primes = []
nums = [True] * n
for i in range(2, n):
    if nums[i]:
        primes.append(i)
        for j in range(i**2, n, i):
            nums[j] = False

def getPrimeFactorization(n):
    f = []
    nth = 0
    while n > 1:
        prime = primes[nth]
        if n % prime == 0:
            f.append(Option(prime, 1))
            n = n // prime
            while n % prime == 0:
                f[-1].count += 1
                n = n // prime
        nth += 1
    return f

def getCombinationsIncrement(index, options, chosen):
    if index >= len(options):
        return False
    else:
        chosen[index] += 1

    if chosen[index] > options[index].count:
        chosen[index] = 0
        return getCombinationsIncrement(index + 1, options, chosen)
    else:
        return True

def getCombinations(options, combine, base):
    combos = [base]
    chosen = [0] * len(options)

    while getCombinationsIncrement(0, options, chosen):
        combos.append(base)

        for i in range(len(options)):
            for _ in range(chosen[i]):
                combos[-1] = combine(combos[-1], options[i].value)

    #combos.sort()

    return combos

def get_divisors(n):
    return getCombinations(getPrimeFactorization(n), mul, 1)

# from operator import mul
# from itertools import chain, combinations
# from functools import reduce
#
# n = 5 * 10**5 + 1
# primes = []
# nums = [True] * n
# for i in range(2, n):
#     if nums[i]:
#         primes.append(i)
#         for j in range(i**2, n, i):
#             nums[j] = False
#
# def prime_factorization(n):
#     for prime in primes:
#         count = 0
#         while n % prime == 0:
#             count += 1
#             n //= prime
#             yield prime
#         if n <= 1:
#             break
#
# def all_subsets(ss):
#     return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))
#
# def curry_reduce(method, base):
#     return lambda array: reduce(array, method, base)
#
# def get_divisors(n):
#     return map(curry_reduce(mul, 1), all_subsets(list(prime_factorization(n))))

from random import randint

def geometricTrick(s):
    d = {}
    d['a'] = {}
    d['b'] = {}
    d['c'] = {}
    for i, l in enumerate(s):
        d[l][i + 1] = True

    count = 0
    for b in sorted(d['b']):
        if b > len(s) // 2:
            break;
        n = b**2
        divs = get_divisors(n)
        print(len(divs))
        for a in divs:
            if a in d['a'] and (n // a) in d['c']:
                count += 1
    return count

if __name__ == "__main__":
    #input()
    #s = input().strip()

    s = ['a'] * (5 * 10**5)
    for i in range(len(s)):
        s[i] = ['a', 'b', 'c'][randint(0, 2)]
    s = "".join(s)
    #print("START")
    print(geometricTrick(s))
    print(s)
