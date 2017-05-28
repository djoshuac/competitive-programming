#!/bin/python3

def sum_xor(n):
    mask = 1
    for _ in range(n):
        mask *= 2
        if mask > n:
            break;
    mask -= 1

    count = 0
    for i in range(n):
      if i + n == i ^ n:
        count += 1

    return count

if __name__ == "__main__":
    n = int(input())
    print(sum_xor(n))
