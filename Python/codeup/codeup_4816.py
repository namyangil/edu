t=int(input())
if t%10!=0:
    print(-1)
else:
    print(int(t/300),end=" ")
    t=t%300
    print(int(t/60),end=" ")
    t=t%60
    print(int(t/10))