#!/bin/python3

def same_occurrances(x, y, numbers):
    occurrences = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers) + 1):
            x_count = 0
            y_count = 0
            for v in numbers[i:j]:
                if v == x:
                    x_count += 1
                elif v == y:
                    y_count += 1
            if x_count == y_count:
                occurrences += 1
    return occurrences

if __name__ == "__main__":
    n, q = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(q):
        x, y = map(int, input().split())
        print(same_occurrances(x, y, numbers))
