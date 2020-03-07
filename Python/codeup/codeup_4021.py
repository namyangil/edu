n_list=list(map(int,input().split()))
temp=0
flag=0
for i in n_list:
    if i%2==1:
        temp+=i
        flag=1
if flag==1:
    print(temp)
else:
    print(-1)