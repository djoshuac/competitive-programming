#!/bin/python3

def same_occurrances(x, y, numbers):
    occurrences = 0
    times = 1
    same = 0
    for v in numbers:
        if v == x:
            same += 1
        elif v == y:
            same -= 1
        if same == 0:
            occurrences += times
            times += 1
    return occurrences

if __name__ == "__main__":
    n, q = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(q):
        x, y = map(int, input().split())
        print(same_occurrances(x, y, numbers))
