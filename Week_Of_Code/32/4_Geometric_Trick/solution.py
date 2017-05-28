#!/bin/python3

from operator import mul

class Option:
    def __init__(self, value, count):
        self.value = value
        self.count = count

n = 5 * 10**5 + 1
primes = []
nums = [[] for _ in range(n)]
for i in range(2, n):
    if nums[i]:
        primes.append(i)
        for j in range(i**2, n, i):
            nums[j].append(False)

from random import randint

def geometricTrick(s):
    d = {}
    d['a'] = {}
    d['b'] = {}
    d['c'] = {}
    for i, l in enumerate(s):
        d[l][i + 1] = True

    count = 0
    for b in d['b']:
        n = b**2
        for a in get_divisors(n):
            if a in d['a'] and (n // a) in d['c']:
                count += 1
    return count

if __name__ == "__main__":
    #input()
    #s = input().strip()

    s = ['a'] * 5 * 10**5
    for i in range(len(s)):
        s[i] = ['a', 'b', 'c'][randint(0, 2)]
    s = "".join(s)
    print(geometricTrick(s))
