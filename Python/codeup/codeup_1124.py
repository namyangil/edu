in_list=input()
len_list=len(in_list)
flag=0
first=""
second=""
for i in range(len_list):
    if in_list[i]=="H":
        flag=i
        break
for i in range(1,flag):
    first+=in_list[i]
for j in range(flag+1,len_list):
    second+=in_list[j]
print(12*int(first)+int(second))