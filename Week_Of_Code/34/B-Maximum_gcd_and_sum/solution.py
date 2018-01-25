#!/bin/python3

import math

def maximum_gcd_sum(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    best = (1, A[0] + B[0])
    for a in A:
        next_a = False
        for i in range(1, math.floor(math.sqrt(a))):
            if a % i == 0:
                j = a // i
                for b in B:
                    if b % j == 0:
                        if j > best[0]:
                            best = (j, a + b)
                            next_a = True
                            break
                    elif b % i == 0:
                        if i > best[0]:
                            best = (i, a + b)
            if next_a:
                break
    return best[1]

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)
