import turtle
wn = turtle.Screen()
t1= turtle.Turtle()

def drawSquareAt(size):
    tracks=list()
    for i in range(4):
        tracks.append(t1.pos())

        t1.fd(size)
        t1.right(90)
    print tracks


def lab7():
    size=90
    drawSquareAt(size)
def main():
    lab7()
if __name__=="__main__": 
     main() 