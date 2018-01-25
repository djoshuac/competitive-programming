N = 1000

grid = []
for i in range(N):
    grid.append(["."] * N)

grid[0][0] = "S"
grid[N-1][N-1] = "T"

for i, row in enumerate(grid):
    if i == N // 2:
        print("".join(["*"] * N))
    else:
        print("".join(row))

