import re
L=[10,2,6,8,1,0]
K=sorted(L)
D={}
for i in xrange(len(K)):
	D[K[i]]=i
for i in xrange(len(L)):
	L[i] = D[L[i]]
print L 
