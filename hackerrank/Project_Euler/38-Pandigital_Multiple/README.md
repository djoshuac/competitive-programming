## Project Euler #38: Double-base Palindromes

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
Let's call 9 as the multiplier, `M`.

The similar process can be shown for 1 to 8 pandigital also. 18 when multiplied
by 1, 2, 3, and 4 gives 18365472 which is 1 to 8  pandigital.

You are given `N` and `K` where  `K`=8 or 9.
Find the multipliers for that given `K` below `N` and print them in ascending order.

[Project Euler 38](https://projecteuler.net/problem=38) - Completed on 24 Sep 2017
[Project Euler+ 38 (hackerrank)](https://www.hackerrank.com/contests/projecteuler/challenges/euler038) - Completed 5 August 2017

-----------

Brute force is plenty fast enough
