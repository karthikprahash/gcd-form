# gcd-form
n,m=input().split()
n=int(n)
m=int(m)
p=[]
q=[]
k=[]
for i in range(1,n+1):
    if n%i==0:
        p.append(i)
for x in range(1,m+1):
    if m%x==0:
        q.append(x)
for g in p:
    if g in q:
        k.append(g)
print(max(k))
        
    
        

