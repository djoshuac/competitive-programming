#from queue import PriorityQueue
from heapq import *
from math import ceil

def solution(n, t, k, d):
    cakes = [0]
    time = 0
    pq = []

    def bakeCakes():
        cakes[0] += k
        heappush(pq, (time + t, "bakeCakes"))
    def makeOven():
        heappush(pq, (time + t, "bakeCakes"))

    heappush(pq, (time + d, "makeOven"))
    heappush(pq, (time + t, "bakeCakes"))

    while cakes[0] < n:
        event = heappop(pq);
        time = event[0]
        if event[1] == "bakeCakes":
            bakeCakes()
        elif event[1] == "makeOven":
            makeOven()

    return ceil(n / k) * t > time

# t time > k carrots
# needs n carrots
# could build 1 extra oven in d

if __name__ == "__main__":
    n, t, k, d = map(int, input().split())
    print("YES" if solution(n, t, k, d) else "NO")
