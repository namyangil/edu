a,b=list(map(int,input().split()))
flag=0
for i in range(a,b+1):
    str_i=str(i)
    len_i=len(str_i)
    for j in range(len_i):
        if str_i[j]=="1":
            flag+=1
print(flag)