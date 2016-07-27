# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, raw_input().split())
ls = [0] * (N+2)
s = 0
rev = True
for i in range(0, M):
    a,b, k = map(int, raw_input().split())
    ls[a] += k
    ls[b+1] -= k
    
s = 0
mx = s
for l in ls:
    s += l
    mx = max(mx, s)
        
#print ls
print mx