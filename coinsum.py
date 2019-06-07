q1,k1=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort(reverse=True)
c1=0
for i1 in range(0,len(l1)):
	if k1>=l1[i1]:
	    r1=k1//l1[i1]
	    c1=c1+r1
	k1=k1%l1[i1]
	if k1==0:
		break
print(c1)
