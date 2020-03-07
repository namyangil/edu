n=int(input())
n_list=list(map(int,input().split()))
new_list=sorted(n_list,reverse=True)
for i in range(n):
    for j in range(n):
        if n_list[i]==new_list[j]:
            print(n_list[i],j+1)
            break