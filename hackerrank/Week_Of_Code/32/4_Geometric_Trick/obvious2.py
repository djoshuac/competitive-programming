#!/bin/python3

from math import sqrt, ceil

def get_divisors(n):
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            yield i

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

    s = ['a'] * 10**5
    for i in range(len(s)):
        s[i] = ['a', 'b', 'c'][randint(0, 2)]
    s = "".join(s)
    print(geometricTrick(s))
