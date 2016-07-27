# Enter your code here. Read input from STDIN. Print output to STDOUT
def isSorted(s):
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

def almostSorted(n, l):
    i = 0
    j = n - 1
    for i in range(0, n-1):
        if(l[i] > l[i+1]):
            break
    for j in range(1, n):
        if(l[n - j] < l[n-j-1]):
            break
    j = n-j
    if isSorted(l):
        print "yes"
    elif isSorted(list(l[:i]) + [l[j]] + list(l[i+1:j]) + [l[i]] + list(l[j+1:])):
        print "yes"
        print "swap " + str(i+1) + " " + str(j+1)
    elif isSorted(l[:i] + l[i:j+1][::-1] + l[j+1:]):
        print "yes"
        print "reverse " + str(i+1) + " " + str(j+1)
    else:
        print "no"
        
        
n = int(raw_input())
l = map(int, raw_input().split(" "))
almostSorted(n, l)

