## Project Euler #36: Double-base Palindromes

Given two integers `N` and `K`,

Find the sum of the natural numbers less than `N` that are palindromes in both
base 10 and base `K`

[Project Euler 31](https://projecteuler.net/problem=36) - Completed on 13 Sep 2016
[Project Euler+ 31 (hackerrank)](https://www.hackerrank.com/contests/projecteuler/challenges/euler036) - Completed 9 July 2017

-----------

Iterate through all the numbers. Check if number is palindrome in base 10,
convert the number to string in given base `K`. Check if that's a palindrome.
Sum up the palindromes in both bases.
