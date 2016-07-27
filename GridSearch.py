#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    done = False
    for i in range(0, R):
        if done:
            break
        for j in range(0, C):
            sol = []
            valid = True
            for i2 in range(0, r):
                if not G[i+i2][j:j+c] == P[i2]:
                    valid = False
                    break
            if valid:
                print "YES"
                done = True
    if not done:
        print "NO"
                    
            
                
                
