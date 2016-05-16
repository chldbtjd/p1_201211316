import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
wn.bgpic("myMaze.gif")
cr=70
point=(100,-100)
center=(point[0],point[1]+cr)
coord=[(-120, 120), (-200, 200)]
p1=(-200,-200)
p2=(-100,-200)

def maze():
	t1.penup()
	t1.setpos(-250,250)
        t1.pendown()	
	addMouse()
	addkeys()
	addexit()
	wn.listen()
	turtle.mainloop()
def inCricle(curpos,radius,center):
	return math.sqrt(math.pow(curpos[0]-center[0],2)+math.pow(curpos[1]-center[1],2))<=radius
		
def inLine(p1,p2,curpos):
    xs=p1[0]
    xe=p2[0]
    ys=p1[1]
    ye=p2[1]
    if(xs>xe):
        xs=p2[0]
        xe=p1[0]
    if(ys>ye):
        ys=p2[1]
        ye=p1[1]
    return xs-1 <= curpos[0] <= xe+1 and ys-1 <= curpos[1] <= ye+1
	
	
def keyup():	
	t1.forward(50)
        curpos=t1.pos()	
        if(isInRectangle(curpos,coord)):
        	t1.write("good")
	if(inCricle(curpos,cr,center)):
		t1.write("good")
	if(inLine(p1,p2,curpos)):
		
		t1.write("good")
		t2.pencolor("Red")
		t2.setpos(p2)
		t2.setpos(p1)
def keydown():
	t1.backward(50)
    	curpos=t1.pos()
	if(isInRectangle(curpos,coord)):
        	t1.write("good")
	if(inCricle(curpos,cr,center)):
		t1.write("good")
	if(inLine(p1,p2,curpos)):
		
		t1.write("good")
		t2.pencolor("Red")
		t2.setpos(p2)
		t2.setpos(p1)
def keyright():
	t1.right(90)
def keyleft():
	t1.left(90)
def addkeys():
    
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
   
	
def addMouse():
   

    wn.onclick(mousegoto)
   
def mousegoto(x,y):
    	curpos=(x,y)
	if(isInRectangle(curpos,coord)):
		t1.setpos(x,y)
		t1.write("good")
        else:
		t1.setpos(x,y)
	if(inCricle(curpos,cr,center)):
		t1.setpos(x,y)
		t1.write("good")
	else:
		t1.setpos(x,y)
	if(inLine(p1,p2,curpos)):
		t1.setpos(x,y)
		t1.write("good")
		t2.pencolor("Red")
		t2.setpos(p2)
		t2.setpos(p1)
	else:
		t1.setpos(x,y)
		
def exitq():
	wn.bye()
def addexit():
	wn.onkey(exitq,"q")


def isInRectangle(curpos,coord):
    
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if(xs>xe):
        xs=coord[1][0]
        xe=coord[0][0]
    if(ys>ye):
        ys=coord[1][1]
        ye=coord[0][1]
    return xs <= curpos[0] <= xe and ys <= curpos[1] <= ye
    
       
        



def lab11_2():
        t1.penup()
       
    	t1.setpos(coord[0])
    	t1.pendown()
    	t1.setpos(coord[0][0],coord[1][1])
    	t1.setpos(coord[1])
    	t1.setpos(coord[1][0],coord[0][1])
    	t1.setpos(coord[0])
    	
        t1.penup()
	t1.setpos(point)
	t1.pendown()
	t1.circle(cr)
	t1.penup()
	t1.setpos(0,0)
    	t1.pendown()
	t2.penup()
	 
    	t2.setpos(p1)	
	t2.pendown()
	t2.setpos(p2)
        maze()    
        addMouse()
        addkeys()
        addexit()
        wn.listen()
        turtle.mainloop()  
        

def main():
    lab11_2()
if __name__=="__main__": 
     main() 