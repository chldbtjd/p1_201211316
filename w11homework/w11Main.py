import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()



def keyup():
	t1.forward(50)
def keydown():
	t1.backward(50)
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
	if(x==50 and y<=50 and y>=0):
		t1.setpos(x,y)
		t1.write("good")
		print "good"
		
	else:
		t1.setpos(x,y)
def exitq():
	wn.bye()
def addexit():
	wn.onkey(exitq,"q")

            
def lab11():	
	t2.penup()
	t2.setposition(50,50)
	t2.pendown()
	t2.setposition(50,00)
	addMouse()
	addkeys()
	addexit()
	wn.listen()
	turtle.mainloop()
def main():
    lab11()
if __name__=="__main__": 
     main() 
