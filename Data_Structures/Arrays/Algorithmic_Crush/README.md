Starting with a list of `n` zeros, add `k` to each index from [`a`, `b`] where 1 <= 'a', 'b' <= `n`.

*Note the indexes are 1 based*

### Input Format

1. `n m`, where `n` is the initial size of the array, and `m` is the number of times to mutations
2. Each row following is a mutation following the form `a b k`. `a` is the starting index, `b` is the ending index, and `k` is the number to add

### Output

Print the maximum value in the list after all the mutations.

### Sample Input

    5 3
    1 2 100
    2 5 100
    2 4 5

### Solution

Start out with: `[0, 0, 0, 0, 0]`
First mutation: `[100, 100, 0, 0, 0]`
Second mutation: `[100, 200, 100, 100, 100]`
Third mutation: `[100, 205, 105, 105, 100]`

Since 205 is the largest value, `205` is the answer.

------------------

The constraints are way too big to solve this problem the obvious way by
simulating each mutation. There also isn't a lot of memory to work with.

A good solution involves keeping track of the differences between elements in
the array. When you add 100 to indexes 3 through 10, index 3 gets 100 larger relative
to index 2 and index 11 gets 100 smaller relative to index 10. Indexes 3-10 all increase
by the same amount, so there is no difference between them. After all of the mutations,
all that's left to do is to figure out which element is the maximum by summing all of
the differences.
