## Project Euler #5: Double-base Palindromes

Find the smallest common multiple of the natural numbers less than \$n\$.

[Project Euler 5](https://projecteuler.net/problem=5) - Completed on 16 Aug 2015
[Project Euler+ 5 (hackerrank)](https://www.hackerrank.com/contests/projecteuler/challenges/euler005) - Completed Nov 2016

-----------

The only factors that matter are each prime's largest power less than \$n + 1\$.

This problem can be solved in \$O(n log{} log{} n) using this insight.

1. Sieve all the primes less than \$n + 1\$
2. Find each primes largest power less than \$n + 1\$
3. Multiply all these powers together
