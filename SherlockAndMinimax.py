# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
A = map(int, raw_input().split())
P, Q = map(int, raw_input().split())


A = sorted(A)

Qd = float("inf")
Pd = float("inf")
for a in A:
    Pd = min(Pd, abs(P - a))
    Qd = min(Qd, abs(Q - a))


#print A

if Pd >= Qd:
    mn = Pd, -1, -1
else:
    mn = Qd, -2, -2

#print mn
for i in range(1, N):
    dist = A[i] - A[i-1]
    if dist % 2 == 1:
        dist -= 1
    dist /= 2
    #print dist
    if (dist > mn[0]) and A[i-1] + dist >= P and A[i-1] + dist <= Q:
        mn = (dist, i, i-1)
    #print mn

if mn[1] == -1:
    result = P
elif mn[1] == -2:
    result = Q
else:
    result = A[mn[2]] + mn[0]
print result
    