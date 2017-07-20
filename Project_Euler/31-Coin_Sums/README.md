## Project Euler #31: Coin Sums

Using coin values of `1, 2, 5, 10, 20, 50, 100, 200`, find how many ways there
are to make change for a given value of `N`.

[Project Euler 31](https://projecteuler.net/problem=31) - Completed on 4 Jul 2017
[Project Euler+ 31 (hackerrank)](https://www.hackerrank.com/contests/projecteuler/challenges/euler031) - Completed April 2017

-----------

To get up to test cases of size `10**5`, use dynamic programming. Knowing how many
ways there are to make change for lower numbers can be very helpful.

For hackerrank it's a good idea to memoize the results since there can be up to
`10**4` tests per test case.
