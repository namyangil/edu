n_list=list(map(int,input().split()))
even_list=[0]
odd_list=[0]
for i in n_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(max(even_list)+max(odd_list))