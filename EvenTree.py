# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, raw_input().split(" "))
tree = {}
ancestors = {}
forest = set()
edges = []
for i in range(0, m):
    v1, v2 = map(int, raw_input().split(" "))
    edges.append((v1, v2))
    forest.add(v1)
    forest.add(v2)

new_len = len(edges) + 1
count = 0
i =0
while i < len(edges):
    new_len = len(edges)
    potential_edges = edges[:i] + edges[i+1:]
    forests = [set()]
    for e in potential_edges:
        v1, v2 = e
        already = False
        for f in forests:
            if (v1 in f) or (v2 in f):
                f.add(v1)
                f.add(v2)
                already = True
                break
        if not already:
            a = set()
            a.add(v1)
            a.add(v2)
            forests.append(a)
    valid = True
    sm = 0
    for f in forests:
        #print f
        sm += len(f)
        if not (len(f) % 2 == 0):
            valid=False
    #print valid and (sm == n)
    if valid and (sm == n):
        edges = potential_edges[:]
        count += 1
    else: i+=1

print count
    
    
    

