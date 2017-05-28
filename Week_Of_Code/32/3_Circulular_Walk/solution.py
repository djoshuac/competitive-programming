#!/bin/python3

def circularWalk(n, s, t, r, g, seed, p):
    dist = 0
    jumps = 0
    for i in range(t):
        
        r = (r * g + seed) % p

if __name__ == "__main__":
    n, s, t = map(int, input().split())
    r_0, g, seed, p = map(int, input().split())
    print(circularWalk(n, s, t, r_0, g, seed, p))
