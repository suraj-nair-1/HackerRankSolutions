# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
A = map(int, raw_input().split())
M = int(raw_input())
B = map(int, raw_input().split())

dc = {}
for num in B:
    if(dc.has_key(num)):
        dc[num] += 1
    else:
        dc[num] = 1
#print dc

for num in A:
    if(dc[num] == 1):
        dc.pop(num, None)
    else:
        dc[num] -= 1
        
result = ""
for key in dc.keys():
    result += str(key) + " "
print result    
    