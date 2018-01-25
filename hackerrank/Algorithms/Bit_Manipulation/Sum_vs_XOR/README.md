# Sum vs XOR

Given `n`, find the number of integers `i < n` such that `i + n == i XOR n`

Test cases are in the range `1 <= n <= 10**15`

-----------

## Solution - `O(log(n))`

Brute force, `O(n)`, can be done by simply checking each natural number less than `n`.

A more elegant solution will note that every number has at least `i = 0` as a
solution, and each 0 digit in `n` results in two possible branches of solutions, namely:

    0 + 0 == 0 and 0 XOR 0 == 0   # i's corresponding digit equals 0
    0 + 1 == 1 and 0 XOR 1 == 1   # i's corresponding digit equals 1

Pseudo code:

- Start `count` at 1
- Double `count` for each 0 digit found in `n`
- Return `count`
