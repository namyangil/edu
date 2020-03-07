a,b,c=list(map(int,input().split()))
temp=0
for i in range(1,a+1):
    if a%i==0 and b%i==0 and c%i==0:
        temp=i
print(temp)