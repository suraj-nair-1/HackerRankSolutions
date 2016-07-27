
def rotate(l):
    assert len(l) == 3
    return [l[-1]] + l[:-1]

def findall(l, sortable, ls):
    #print l
    sortable.add(str(l))
    if l == ls:
        return True
    result = False
    for i in range(0, len(l)-2):
        new = l[:i] + rotate(l[i:i+3]) + l[i+3:]
        if str(new) not in sortable:
            result = result or findall(new, sortable, ls)
    return result
    
    
num_tests = int(raw_input())
for a in range(0, num_tests):
    n = int(raw_input())
    ls = map(int, raw_input().split())
    inversions = 0
    for i in range(0, len(ls)):
        for j in range(i, len(ls)):
            if ls[i] > ls[j]:
                inversions += 1
    if inversions % 2 == 0:
        print "YES"
    else:
        print "NO"
        
    
        
    
    