#!/bin/python

import sys

def merge_list(left,right,c):
    result=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            #print "Left result",result
            i=i+1
        elif left[i] > right[j]:
            result.append(right[j])
            #print "Right result",result
            c += len(left[i:])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    #print "Inversions: ",c
    return result,c


def sort_and_count(lis,count):

    if len(lis)<2:
        return lis, count
    middle=len(lis) / 2
    left,c1=sort_and_count(lis[:middle],count)
    #print "left",left
    right,c2=sort_and_count(lis[middle:],count)
    #print "right",right
    m,c=merge_list(left,right,count)
    c=c+c1+c2
    return m,c


T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    inv = 0
    tc = False
    for i in range(0, len(q)-1):
        if q[i] - (i+1) > 2:
            tc = True
    if tc:
        print "Too chaotic"
    else:
        s, inv = sort_and_count(q, 0)
        print inv
    


    # your code goes here
