n,r=list(map(int,input().split()))
a=1
for i in range(1,n+1):
    a*=i
b=1
for i in range(1,r+1):
    b*=i
c=1
for i in range(1,n-r+1):
    c*=i
print(int(a/(b*c)))