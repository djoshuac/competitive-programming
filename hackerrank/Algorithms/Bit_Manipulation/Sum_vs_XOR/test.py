#!/bin/python3

from solution import sum_xor as solution
from brute import sum_xor as brute

if __name__ == "__main__":
    for n in range(1, 5000):
        a, b = solution(n), brute(n)
        if a != b:
            print(n, a, b)
