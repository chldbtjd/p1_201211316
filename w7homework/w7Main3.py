import turtle
wn=turtle.Screen()
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

def drawSquareForm(tracks):
   
    
    t1.home()
    for i in range(0,4):
        t1.setpos(tracks[i])
    t1.clear()

        
    


   
   


def saveTracks():
    tracks=list()
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.penup()
    t1.clear()
    
    return tracks
    


def replayTracks(tracks):
    
    for i in range (0,len(tracks)):
        
        t1.setpos(tracks[i])
        t1.pendown()

        
def lab7_1():
    pos=(0.00,0.00)
    size=90
    mytracks=drawSquareAt(size,pos)
    print mytracks
    
    tracks=list()
    
    pos1=(90.00,0.00)
    pos2=(90.00,-90.00)
    pos3=(00.00,-90.00)
    pos4=(0.00,0.00)

    tracks.append(pos1)
    tracks.append(pos2)
    tracks.append(pos3)
    tracks.append(pos4)
    drawSquareForm(tracks)
    


def lab7_2():
    my=saveTracks()
    print my
    replayTracks(my)
def main():
    lab7_1()
    lab7_2()
if __name__=="__main__": 
     main() 