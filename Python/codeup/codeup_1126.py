in_list=[]
temp=0
for i in range(3):
    in_list.append(list(map(float,input().split())))
for j in range(3):
    temp+=in_list[j][0]*in_list[j][1]
print("{:0.1f}".format(temp))