y,m,d=list(map(str,input().split("/")))
md=m+d
y_list=[]
md_list=[]
for i in range(4):
    y_list.append(y[i])
    md_list.append(md[i])
y_list.sort()
md_list.sort()
if y_list==md_list:
    print("yes")
else:
    print("no")