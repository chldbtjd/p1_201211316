import turtle
wn = turtle.Screen()
t1= turtle.Turtle()

a=raw_input("triangle or square:")
size =100
def drawTriangleAt(size):
    for i in range(3):
        t1.fd(size)
        t1.right(120)
def drawSquareAt(size):
    for i in range(4):
        t1.fd(size)
        t1.right(90)
if(a=='T'):
   drawTriangleAt(size)
    
elif(a=='S') :
    drawSquareAt(size)
else :
    print "Error"