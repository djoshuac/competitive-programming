def prime_sieve(n):
    is_prime = [True] * n

    for i in range(2, n):
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False
            yield i

def power_less_than(n, m):
    p = n
    while p < m:
        p *= n
    return p // n

def smallest_multiple(n):
    answer = 1
    for p in prime_sieve(n + 1):
        answer *= power_less_than(p, n + 1)
    return answer

if __name__ == "__main__":
    n = int(input())
    print(smallest_multiple(n))
