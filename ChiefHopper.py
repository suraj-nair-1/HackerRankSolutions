# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
ls = map(int, raw_input().split())
initial = 0
e = initial
i = 0
while i < N:
    if ls[i] > e:
        e -= (ls[i] - e)
    else:
        e += (e - ls[i])
    #print e
    if e < 0:
        initial += 1
        e = initial
        i = 0
    else:
        i += 1
        
print initial
    