#!/bin/python3

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
        for a in d['a']:
            if (n // a) in d['c'] and n % a == 0:
                count += 1
    return count

if __name__ == "__main__":
    input()
    s = input().strip()
    print(geometricTrick(s))
