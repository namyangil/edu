n=int(input())
n_list=[]
for i in range(n):
    n_list.append(input())
flag=""
len_i=0
for i in n_list:
    flag=i
    while int(flag)>9:
        len_i=len(flag)
        temp=0
        for j in range(len_i):
            temp+=int(flag[j])
        flag=str(temp)
    print(flag)