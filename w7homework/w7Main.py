import turtle
wn = turtle.Screen()
t1= turtle.Turtle()

def drawSquareAt(size,pos):
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(4):
        tracks.append(t1.pos())

        t1.fd(size)
        t1.right(90)
    return tracks


def lab7():
    pos=(0.00,0.00)
    size=90
    mytracks=drawSquareAt(size,pos)
    print mytracks
def main():
    lab7()
if __name__=="__main__": 
     main() 