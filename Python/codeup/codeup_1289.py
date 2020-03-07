a1,a2=list(map(int,input().split()))
b1,b2=list(map(int,input().split()))
c1,c2=list(map(int,input().split()))
temp=[]
temp.append(a1*a2)
temp.append(b1*b2)
temp.append(c1*c2)
print(max(temp))