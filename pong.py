import turtle

win=turtle.Screen()
win.title("Pong game by Soutrik Pal")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)                         #stops window from updating


score_a=0
score_b=0

#Creating shapes and the objects of the game
#Paddle A
paddle_a=turtle.Turtle()              #turtle object
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B

paddle_b=turtle.Turtle()              #turtle object
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)

#Ball

ball=turtle.Turtle()              #turtle object
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_wid=2,stretch_len=2)
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=1                                    #this is for starting the movement of the ball



name=turtle.Turtle()
name.speed(0)
name.color("yellow")
name.penup()
name.goto(0,270)
name.write("Pong game by Soutrik",align="center",font=("Courier",24,"normal"))

#Creating the scoring system
score=turtle.Turtle()
score.speed(0)
score.color("red")
score.penup()
score.goto(0,-260)
score.write("Player A=0 Player =0",align="center",font=("courier",18,"normal"))


#Movement of objects
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+80
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-80
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y=y+80
    paddle_b.sety(y)   

def paddle_b_down():
    y=paddle_b.ycor()
    y=y-80
    paddle_b.sety(y) 





#Keyboard mapping
win.listen()                        #listens to input from keyboard
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"8")
win.onkeypress(paddle_b_down,"2")



while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)           #movement of ball using this loop
    ball.sety(ball.ycor()+ball.dy)


    #bouncing back from screen borders
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy  *=-1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy  *=-1    

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
      
       

        
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *=-1   
       
        



    if (ball.xcor() >340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *=-1

    if(ball.xcor()>-350 and ball.xcor()<-340) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()> paddle_a.ycor() -50 ):
       ball.setx(-340)
       ball.dx *=-1