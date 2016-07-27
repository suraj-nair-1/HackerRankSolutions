# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b, num = map(int, raw_input().split())
dc = {}
dc[1] = a
dc[2] = b

def T(n):
    if dc.has_key(n):
        return dc[n]
    dc[n] = (T(n-1)*T(n-1)) + T(n-2)
    return dc[n]

print T(num)
    