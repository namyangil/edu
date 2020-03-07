code=input()
a,b,c=input().split()
n=0
def find_pwd(x):
    n=len(x)
    for i in range(n):
        for j in range(10):
            if x[i]==code[j]:
                print(j,end="")
                break
    print(" ",end="")
find_pwd(a)
find_pwd(b)
find_pwd(c)