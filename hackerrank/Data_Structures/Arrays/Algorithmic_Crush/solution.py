#!/bin/python3

if __name__ == "__main__":
    n, m = map(int, input().split())
    diffs = [0] * (n + 1)

    for _ in range(m):
        a, b, k = map(int, input().split())
        diffs[a - 1] += k
        diffs[b] -= k

    last = 0
    most = 0
    for d in diffs:
        last += d
        if last > most:
            most = last

    print(most)
