n=int(input())
n_list=[]
for i in range(1,n+1):
    flag=1
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
    if flag==1:
        n_list.append(i)
print(sum(n_list)-1)