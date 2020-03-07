in_list=input()
len_list=len(in_list)
temp=0
for i in range(len_list):
    temp+=int(in_list[i])
if temp%7==4:
    print("suspect")
else:
    print("citizen")