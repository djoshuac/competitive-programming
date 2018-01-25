from solution import min_squares

def test(canvas, length, width, expected):
    got = min_squares(canvas, length, width)
    if got != expected:
        print("Failed for", canvas, "  expected=", expected, "  but got=", got)

test([
"WWWW",
"WWWB",
"WWWB",
"WWBB",
"WWWW"
], 5, 4, 5)

test([
"WWWW",
"WWWB",
"WWWB",
"WWBB",
"WWWB"
], 5, 4, 11)

test([
"BB"
], 1, 2, -1)

test([
"B"
], 1, 1, 0)

test([
"W"
], 1, 1, 1)


test([
"WW"
], 1, 2, 1)

test([
"BWWWB",
"WWWWW",
"WWWWW",
"WWWWW",
"BWWWB"
], 5, 5, 21)

test([
"WWWWB",
"WWWWW",
"WWBWW",
"WWWWW",
"BWWWB"
], 5, 5, 21)


test([
"WWWWB",
"WWWWW",
"WWWWW",
"WWWWW",
"BWWWW"
], 5, 5, 23)

test([
"WBWW",
"BWBW",
"WWWB",
], 3, 4, -1)

test([
"BWWWBW",
"WWWWWW",
"WWWWWW",
"WWWWWW",
"BWWWBB"
], 5, 6, -1)
