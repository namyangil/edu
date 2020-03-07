k,n=list(map(int,input().split()))
k_list=[]
k_list.append(list(map(int,input().split())))
new_list=k_list[0]
while len(new_list)<n:
    len_k=len(new_list)
    new_list.append(sum(new_list[len_k-k:len_k]))
print(new_list[n-1])