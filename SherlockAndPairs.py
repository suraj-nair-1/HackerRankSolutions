# Enter your code here. Read input from STDIN. Print output to STDOUT

num_cases = int(raw_input())
for i in range(0, num_cases):
    n = int(raw_input())
    l = map(int, raw_input().split(" "))
    dct = {}
    for num in l:
        if dct.has_key(num):
            dct[num] += 1
        else:
            dct[num] = 1
    s = 0
    for key in dct.keys():
        Nn = dct[key]
        if Nn > 1:
            s += (Nn) * (Nn - 1)
    print s
        
        
        
    