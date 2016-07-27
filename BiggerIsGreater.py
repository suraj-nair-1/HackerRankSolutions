# Enter your code here. Read input from STDIN. Print output to STDOUT
def swap(s, i, j):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))


def bigger(s):
    j = len(s) - 2
    while(j >= 0):
        rng = range(j+1, len(s))
        rng.reverse()
        for k in rng:
            cons = s[k]
            if cons > s[j]:
                
                return swap(s, j, k)
        j = j - 1
    return "no answer"
        

num_cases= int(raw_input())
for k in range(0, num_cases):
    s = raw_input()
    a = bigger(s)
    solution = a
    if not (a == "no answer"):
        for i in range(0, len(s)):
            if s[i] < a[i]:
                solution = a[0:i+1] + "".join(sorted(a[i+1:])).replace("\n", "")
    print solution


