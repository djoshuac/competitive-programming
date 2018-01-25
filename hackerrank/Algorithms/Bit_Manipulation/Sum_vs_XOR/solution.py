#!/bin/python3

def sum_xor(n):
    count = 1
    for _ in range(n):
        if n == 0:
            break;
        if n % 2 == 0:
            count *= 2
        n //= 2
    return count

if __name__ == "__main__":
    n = int(input())
    print(sum_xor(n))
