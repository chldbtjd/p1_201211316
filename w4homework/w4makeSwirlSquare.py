import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
size =50
angle = 90
bigger = 10
sides =10

def makeSwirlSquare(size,bigger,sides,angle):
    for i in range(sides):
        if(i%2):
            size=size+bigger
        t1.fd(size)
        t1.right(angle)
       
        

makeSwirlSquare(size,bigger,sides,angle)
        