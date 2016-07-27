# Enter your code here. Read input from STDIN. Print output to STDOUT
num_tests = int(raw_input())
for i in range(0, num_tests):
    n = int(raw_input())
    l = map(int, raw_input().split(" "))
    
    noncont = max(l[0], 0)
    maxSoFar = l[0]
    mx = l[0]
    for j in range(1, n):
        maxSoFar = max(l[j], l[j] + maxSoFar)
        mx = max(mx, maxSoFar)
        if(l[j] > 0):
            noncont += l[j]
    if noncont == 0:
        noncont = mx
   
    print mx, noncont
    
    