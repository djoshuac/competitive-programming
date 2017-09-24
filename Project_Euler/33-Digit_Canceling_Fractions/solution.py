raise "INCOMPLETE https://www.hackerrank.com/contests/projecteuler/challenges/euler033"

if __name__ == "__main__":
    n, base = map(int, input().split())
    print(double_base_palindrome_sum(n, base))
