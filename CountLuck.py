# Enter your code here. Read input from STDIN. Print output to STDOUT

def alg(forest, visited, current, finish, count, n, m):
    if(current == finish):
        return count, True
    i, j = current
    visited[current] = 1
    options = {}
    options[(i,j+1)] = 1
    options[(i,j-1)] = 1
    options[(i+1,j)] = 1
    options[(i-1,j)] = 1
    for option in options.keys():
        if option[0] >= n or option[0] < 0 or option[1] >= m or option[1] < 0:
            options.pop(option, None)
        elif visited.has_key(option):
            options.pop(option, None)
        elif forest[option[0]][option[1]] == "X":
            options.pop(option, None)

    if len(options) > 1:
        for option in options.keys():
            ct, crrct = alg(forest, visited, option, finish, count + 1, n, m)
            if crrct:
                return ct, crrct
        return count, False
    else:
        for option in options:
            ct, crrct = alg(forest, visited, option, finish, count, n, m)
            if crrct:
                return ct, crrct
        return count, False
    

num_cases = int(raw_input())
for q in range(0, num_cases):
    n, m = map(int, raw_input().split(" "))
    forest = [""] * n
    for rows in range(0, n):
        forest[rows] = raw_input()
        for j in range(0, m):
            if(forest[rows][j] == "M"):
                current = (rows, j)
            if(forest[rows][j] == "*"):
                finish = (rows, j)
    guess = int(raw_input())
    visited = {}
    
    
    if alg(forest, visited, current, finish, 0, n, m)[0] == guess:
        print "Impressed"
    else:
        print "Oops!"
    
    