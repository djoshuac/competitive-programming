### Black square

1. Given a grid of "W" and "B" (symbolizing white and black squares)

Find the minimum number of white squares needed to be painted black to create a
single black square.

E.G

    WBBW      BBBW
    BWBW  ->  BBBW
    BBBW      BBBW

    // two squares painted

If it's impossible return -1

-------------

I hardcoded a lot of this problem since it was faster than coming up with a
generalization.

Solution:

1. Find the topmost, leftmost, rightmost, bottommost black squares locations
2. Count the number of white squares contained
3. Add walls until the shape is square
4. If you can't add another wall, and the shape not yet a square return -1
