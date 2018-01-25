#!/bin/python3

def maximum_gcd_sum(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(max(A[0], B[0]), 1, -1):
        for a in A:
            if a % i == 0:
                for b in B:
                    if b % i == 0:
                        return a + b
                break

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)
