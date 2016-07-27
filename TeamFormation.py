# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

def update(dc, item):
    sz = 0
    if dc.has_key(item-1):
        tms = dc[item-1]
        if len(tms) == 1:
            sz = tms[0]
            dc.pop(item-1, None)
        else:
            sz = min(tms)
            tms.remove(sz)
    if dc.has_key(item):
        s = dc[item]
        s.append(sz+1)
        dc[item] = s
    else:
        dc[item] = [sz+1]
            
    

num_test = int(raw_input())
for i in range(0, num_test):
    input = map(int, raw_input().split())
    n = input[0]
    l = input[1:]
    l = sorted(l)

    dc = {}
    
    for elem in l:
        update(dc, elem)
        
    #print dc.values()
    vals = [item for sublist in dc.values() for item in sublist]
    
    if dc == {}:
        print 0
    else:
        result = min(vals)
        print result
   
    