# Enter your code here. Read input from STDIN. Print output to STDOUT
num_tests = int(raw_input())
for test in range(0, num_tests):
    m, n = map(int, raw_input().split())
    y_costs = map(int, raw_input().split())
    x_costs = map(int, raw_input().split())
    
    y_count = 1
    x_count = 1
    
    s = 0

    y_costs = sorted(y_costs)
    x_costs = sorted(x_costs)
    
    while (len(y_costs) != 0) or (len(x_costs) != 0):
        
        if len(y_costs) == 0:
            s += (x_count * x_costs[-1])
            x_costs.pop()
            y_count += 1
        elif len(x_costs) == 0:
            s += (y_count * y_costs[-1])
            y_costs.pop()
            x_count += 1
        elif y_costs[-1] > x_costs[-1]:
            s += (y_count * y_costs[-1])
            y_costs.pop()
            x_count += 1
        else:
            s += (x_count * x_costs[-1])
            x_costs.pop()
            y_count += 1
        
    print s % (10**9 + 7)
    
