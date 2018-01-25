### Reconstruct a string from memory

1. Given a list of substrings of the solution
2. And the positions where those substrings occur in the solution

Find the lexicographically smallest string that matches the given substrings
and positions. There is always guaranteed to be a solution.

-------------

This was tougher to solve in python since I had to learn how to use byte arrays
in python 3 (python strings are immutable so there would be way to much work
done with  a maximum of 10**5 substrings).

Solution:

1. Find the length of the solution by checking each substring and its max position
2. Fill a `bytearray` with `'a'` of the given length so it will be lexicographically the smallest
3. Iterate through the substrings and overlay them into the byte array at each of their positions
4. Return the bytearray as a string
