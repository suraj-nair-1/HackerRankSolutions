# Enter your code here. Read input from STDIN. Print output to STDOUT

def bestOption(current_price,money, num_stocks, ls):
    if len(ls) == 0:
        return max(money, money + (num_stocks * current_price), money - (current_price))
    doNothing = bestOption(ls[0],money, num_stocks, ls[1:])
    sell = bestOption(ls[0], money + (num_stocks * current_price), 0, ls[1:])
    buy = bestOption(ls[0], money - (current_price), num_stocks + 1, ls[1:])
    return max(doNothing, sell, buy)

num_tests = int(raw_input())
for nm in range(0, num_tests):
    n = int(raw_input())
    l = map(int, raw_input().split(" "))
    num_stocks  = 0
    max_ahead = 0
    sol = []
    for i in reversed(range(0, n)):
        max_ahead = max(max_ahead, l[i])
        sol.append((l[i], max_ahead))
    sol.reverse()
    money = 0
    num_stock = 0
    for res in sol:
        if res[0] < res[1]:
            money -= res[0]
            num_stock += 1
        else:
            if num_stock > 0:
                money += (num_stock * res[0])
                num_stock = 0
    print money
    
            
            
            
            
            
        