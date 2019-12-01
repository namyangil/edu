from time import sleep
for i in range(10):
    msg="\r 진행률 %d%%"%(i+1)
    print(""*len(msg),end="")
    print(msg,end="")
    sleep(0.1)


# \r 캐리지 리턴 문자가 ♪로 인식되고 있음.
