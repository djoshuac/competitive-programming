from brute import distinct_powers_count as brute
from solution import distinct_powers_count as solution

if __name__ == "__main__":
    for n in range(100):
        b = brute(n)
        s = solution(n)
        if b != s:
            print(n, ":", b, s)
