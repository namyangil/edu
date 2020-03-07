n=int(input())
temp=0
flag=0
for i in range(1,int(n/3)+1):
    for j in range(i,int(n/2)+1):
        temp=n-i-j
        if temp<i+j and temp>=j:
            flag+=1
print(flag)