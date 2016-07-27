# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(raw_input())
n = int(raw_input())


def search(ones, grid, pos):
    neighbors = []
    
    i, j = pos
    grid[i][j] = 0
    ones.remove((i,j))
    sz = 1
    if i < m-1:
        if(grid[i+1][j] == 1):
            sz += search(ones, grid,(i+1, j))
    if i > 0:
        if(grid[i-1][j] == 1):
            sz += search(ones, grid,(i-1, j))
    if j < n-1:
        if(grid[i][j+1] == 1):
            sz += search(ones, grid,(i, j+1))
    if j > 0:
        if(grid[i][j-1] == 1):
            sz += search(ones, grid,(i, j-1))
    if i < m-1 and j < n-1:
        if(grid[i+1][j+1] == 1):
            sz += search(ones, grid,(i+1, j+1))
    if i > 0 and j < n-1:
        if(grid[i-1][j+1] == 1):
            sz += search(ones, grid,(i-1, j+1))
    if i < m-1 and j > 0:
        if(grid[i+1][j-1] == 1):
            sz += search(ones, grid,(i+1, j-1))
    if i > 0 and j > 0:
        if(grid[i-1][j-1] == 1):
            sz += search(ones, grid,(i-1, j-1))

    return sz

grid = []
ones = []
for i in range(0, m):
    row = map(int, raw_input().split())
    for r in range(0, n):
        if row[r] == 1:
            ones.append((i, r))
    grid.append(row)

#print grid
#print ones
result = 0
while len(ones) > 0:
    result = max(result, search(ones, grid, ones[0]))
print result
    