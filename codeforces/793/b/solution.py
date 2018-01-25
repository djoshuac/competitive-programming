# changed
def answer(grid):
    def find(type):
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == type:
                    return (i, j)
        return (-1, -1)

    home = find("S")
    work = find("T")

    # mark 0 turns away from work
    for i in range(work[0], -1, -1):
        if grid[i][work[1]] == "*":
            break;
        grid[i][work[1]] = "0"
    for i in range(work[0], len(grid)):
        if grid[i][work[1]] == "*":
            break;
        grid[i][work[1]] = "0"
    for j in range(work[1], -1, -1):
        if grid[work[0]][j] == "*":
            break;
        grid[work[0]][j] = "0"
    for j in range(work[1], len(grid[0])):
        if grid[work[0]][j] == "*":
            break;
        grid[work[0]][j] = "0"

    # check to get to  0 turns away from work
    for i in range(home[0], -1, -1):
        if grid[i][home[1]] == "*":
            break;
        x, y = i, home[1]

        for xi in range(x, -1, -1):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for xi in range(x, len(grid)):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for yi in range(y, -1, -1):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        for xi in range(y, len(grid[0])):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        
    for i in range(home[0], len(grid)):
        if grid[i][home[1]] == "*":
            break;
        x, y = i, home[1]
        
        for xi in range(x, -1, -1):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for xi in range(x, len(grid)):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for yi in range(y, -1, -1):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        for xi in range(y, len(grid[0])):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        
    for j in range(home[1], -1, -1):
        if grid[home[0]][j] == "*":
            break;
        x, y = home[0], j

        for xi in range(x, -1, -1):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for xi in range(x, len(grid)):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for yi in range(y, -1, -1):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        for xi in range(y, len(grid[0])):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        
    for j in range(home[1], len(grid[0])):
        if grid[home[0]][j] == "*":
            break;
        x, y = home[0], j
        
        for xi in range(x, -1, -1):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for xi in range(x, len(grid)):
            if grid[xi][y] == "*":
                break;
            if grid[xi][y] == "0":
                return "YES"
        for yi in range(y, -1, -1):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"
        for xi in range(y, len(grid[0])):
            if grid[x][yi] == "*":
                break;
            if grid[x][yi] == "0":
                return "YES"

    return "NO"
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    print(answer(grid))
