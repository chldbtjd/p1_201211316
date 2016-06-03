import turtle

import math
import random
speed = 1
def main():
    
    playCheck = raw_input("Do you want to play the Turtle game?(y or n) ")
    if playCheck.lower()=="y":
     
        turtle.setup(700,700)
        wn = turtle.Screen()
        wn.bgcolor("light green")
        wn.tracer(1)

        border = turtle.Turtle()
        border.color("black")
        border.penup()
        border.setposition(-300,-300)
        border.pendown()
        border.pensize(3)
        for line in range(4):
            border.forward(600)
            border.left(90)
        border.hideturtle()
     

        player = turtle.Turtle()
        player.color("black")
        player.shape("turtle")
        player.penup()
        player.speed(0)


        food = turtle.Turtle()
        food.shape("circle")
        food.color("red")
        food.penup()
        food.speed(0)
        food.setposition(random.randint(-290,290),random.randint(-290,290))
        
        def turnLeft():
            player.setheading(180)

        def turnRight():
            player.setheading(0)

        def turnUp():
            player.setheading(90)

        def turnDown():
            player.setheading(270)

        def increaseSpeed():
            global speed
            speed+=0.1
        

        turtle.listen()
        turtle.onkey(turnLeft,"Left")
        turtle.onkey(turnRight,"Right")
        turtle.onkey(turnUp,"Up")
        turtle.onkey(turnDown,"Down")


        score = 0
        count = 0
        pen1 = turtle.Turtle()
        pen2 = turtle.Turtle()


        def pena():
            pen1.hideturtle()
            pen1.penup()
            pen1.setposition(-290,310)
            pen1script = "Score: %d" %score
            pen1.write(pen1script,False,align="left", font=("Arial",14,"normal"))

  

        def penb():
            pen2.hideturtle()
            pen2.penup()
            pen2.setposition(290,310)
            pen2script = "%d attempts remaining."%(3-int(count))
            pen2.write(pen2script, False, align="right", font=("Arial",14,"normal"))
            
      


        def collision(p,f):
            d = math.sqrt(math.pow(p.xcor()-f.xcor(),2)+math.pow(p.ycor()-f.ycor(),2))
            if d<20:
                return True
            else:
                return False
        
       
        pena()
        penb()

 
        while True:
            player.forward(speed)

            if count>=3:
                break

            if -290>player.xcor() or player.xcor()>290:
                count+=1
                pen2.undo()
                penb()
                turtle.ontimer(player.setposition(0,0),1500)
            if -290>player.ycor() or player.ycor()>290:
                count+=1
                pen2.undo()
                penb()
                turtle.ontimer(player.setposition(0,0),1500)
            if collision(player,food):
                score+=10
                pen1.undo()
                pena()
                increaseSpeed()
                food.setposition(random.randint(-290,290),random.randint(-290,290))

        pen2.setposition(0,0)        
        pen2script = "Your final score: %d." %score
        pen2.write(pen2script, False, align = "center",font=("Arial",20,"normal"))

    elif playCheck.lower()=="n":
        print("Thank you")
    else:
        print("try agian")
        main()

main()

