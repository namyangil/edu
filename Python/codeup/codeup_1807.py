a,b=list(map(int,input().split()))
max_num=0
max_len=0
for x in range(a,b+1):
    flag=1
    temp=x
    while x!=1:
        if x%2==1:
            x=3*x+1
        else:
            x=x/2
        flag+=1
    if flag>max_len:
        max_len=flag
        max_num=temp
print(max_num,max_len)