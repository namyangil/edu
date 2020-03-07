a,b=list(map(int,input().split()))
flag=[]
for i in range(1,a+1):
    if a%i==0:
        flag.append(i)
for j in range(1,b+1):
    if b%j==0:
        flag.append(j)
flag=list(set(flag))
flag.sort()
for i in range(len(flag)):
    print(flag[i],end=" ")