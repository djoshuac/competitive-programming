#!/bin/python3

def gcd(a, b):
    a, b = (b, a) if a < b else (a, b)
    while b != 0:
        a %= b
        a, b = b, a
    return a

def maximum_gcd_sum_brute(A, B):
    gs = (0, 0)
    for a in A:
        for b in B:
            ab = (gcd(a, b), a + b)
            if ab[0] > gs[0]:
                gs = ab
            elif ab[0] == gs[0] and ab[1] > gs[1]:
                gs = ab
    return gs[1]

if __name__ == "__main__":
    n = int(input()) # skip n

    A = {}
    B = {}

    for a in map(int, input().strip().split()):
        A[a] = True
    for b in map(int, input().strip().split()):
        B[b] = True

    res = maximum_gcd_sum_brute(A.keys(), B.keys())
    print(res)
