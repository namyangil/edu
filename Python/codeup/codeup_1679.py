n=int(input())
n_list=[]
for i in range(1,int(n/2)+1):
    for j in range(i,int(n/2)+1):
        x=n-i-j
        if i+j>x and x>=j:
            n_list.append([i,j,n-(i+j)])
if len(n_list)==0:
    print(-1)
for i in n_list:
    print(" ".join(map(str,i))) #리스트를 문자열로 출력하기