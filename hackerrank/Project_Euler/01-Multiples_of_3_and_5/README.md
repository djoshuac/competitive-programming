## Project Euler #1: Multiples of 3 and 5

Find the sum of all numbers divisible by 3 or 5 (no repeats) below N.

[Project Euler 1](https://projecteuler.net/problem=1) - Completed on 15 Aug 2015
[Project Euler+ 1 (hackerrank)](https://www.hackerrank.com/contests/projecteuler/challenges/euler001) - Completed Jan 2017

-----------

This problem is brilliant. It's similar to fizz buzz, and for Project Euler one
can simply add up all the multiples of 3, then add up all the multiples of 5,
sum those values together and subtract the multiples of 15.

However, to pass the hackerrank test cases, one needs to utilize the symmetric
sum for triangular numbers:

    triangular(n) = n * (n - 1) / 2
