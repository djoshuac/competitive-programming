import random
#
# def test(canvas, length, width, expected):
#     got = min_squares(canvas, length, width)
#     if got != expected:
#         print("Failed for", canvas, "  expected=", expected, "  but got=", got)

num_lines = 10**5
print(num_lines)
for i in range(num_lines):
    line = ["aaaaaaaaaa"]
    last = 1
    values = []
    for j in range(random.randint(0, 10) + 1):
        last = random.randint(1, 10**6 - 500)
        values.append(last)

    print(" ".join(line + [str(len(values))] + list(map(str, sorted(values)))))
