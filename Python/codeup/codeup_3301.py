n=int(input())
flag=0
flag+=int(n/50000)
n=n%50000
flag+=int(n/10000)
n=n%10000
flag+=int(n/5000)
n=n%5000
flag+=int(n/1000)
n=n%1000
flag+=int(n/500)
n=n%500
flag+=int(n/100)
n=n%100
flag+=int(n/50)
n=n%50
flag+=int(n/10)
print(flag)