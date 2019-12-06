import turtle as t

def 위():
    t.setheading(90)
    t.fd(10)

def 아래():
    t.setheading(270)
    t.fd(10)
def 왼쪽():
    t.setheading(180)
    t.fd(10)
def 오른쪽():
    t.setheading(0)
    t.fd(10)
def 지우기():
    t.clear()
    
t.shape("turtle")
t.speed(0)
t.onkeypress(위,"Up")
t.onkeypress(아래,"Down")
t.onkeypress(왼쪽,"Left")
t.onkeypress(오른쪽,"Right")
t.onkeypress(지우기,"Escape")

t.listen()
