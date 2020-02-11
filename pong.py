import turtle #graphics library
from playsound import playsound
import os

wn_width = 800
wn_height = 600
wn = turtle.Screen() #window
wn.title("Pong Boi")
wn.bgcolor("black")
wn.setup(width=wn_width, height=wn_height)
wn.tracer(0) #stops window from constantly updating; runs game faster

#***Score
score_a = 0
score_b = 0

#***Paddle A (left)
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation; maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #stretches width from default 20 to 20*5
paddle_a.penup() #dont draw a line as you're moving (by default)
paddle_a.goto(-350, 0) #vertically centered

#***Paddle B (right)
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation; maximum possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #stretches width from default 20 to 20*5
paddle_b.penup() #dont draw a line as you're moving (by default)
paddle_b.goto(350, 0) #vertically centered

#***Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation; maximum possible speed
ball.shape("square")
ball.color("white")
ball.penup() #dont draw a line as you're moving (by default)
ball.goto(0, 0) #vertically centered
ball.dx = 0.13 #change (speed) in x 
ball.dy = 0.13 # change (speed) in y 
ball_xsize = 20 #for logic
ball_ysize = 20 #for logic

#***Pen (turtle)
pen = turtle.Turtle()
pen.speed(0) #animation speed
pen.color("white")
pen.penup() #dont draw a line as you're moving
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


#***Movement FunctionS
def paddle_a_up():
	y = paddle_a.ycor() #from turtle library
	y += 20
	paddle_a.sety(y)
	
def paddle_a_down():
	y = paddle_a.ycor() #from turtle library
	y -= 20
	paddle_a.sety(y)
	
def paddle_b_up():
	y = paddle_b.ycor() #from turtle library
	y += 20
	paddle_b.sety(y)
	
def paddle_b_down():
	y = paddle_b.ycor() #from turtle library
	y -= 20
	paddle_b.sety(y)
	

#***keyboard/screen events
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#***Main game loop
while True:
	wn.update() #update screen everytime loop runs
	
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	
	#***Move ball & If ball hits border & scoring
	
	#right side
	if ball.xcor() > ((wn_width/2)-(ball_xsize/2)):
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, 'oof.wav')
		playsound(filename)
		
	#left side
	if ball.xcor() < -((wn_width/2)-(ball_xsize/2)):
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, 'oof.wav')
		playsound(filename)
	
	#top side
	if ball.ycor() > ((wn_height/2)-(ball_ysize/2)):
		ball.sety(((wn_height/2)-(ball_ysize/2)))
		ball.dy *= -1
	
	#bottom side
	if ball.ycor() < -((wn_height/2)-(ball_ysize/2)):
		ball.sety(-((wn_height/2)-(ball_ysize/2)))
		ball.dy *= -1
		
	#***paddle collision with top & bottom
	
	#limit paddle_a's y if it hits (max window +y Coordinate - paddle height); top
	if paddle_a.ycor() > (300-50):
		paddle_a.sety(300-50)
	
	#limit paddle_b's y if it hits (max window +y Coordinate - paddle height); top
	if paddle_b.ycor() > (300-50):
		paddle_b.sety(300-50)
		
	#limit paddle_a's y if it hits (min window -y Coordinate -  paddle height); bottom
	if paddle_a.ycor() < (-300+50):
		paddle_a.sety(-300+50)
		
	#limit paddle_b's y if it hits (min window -y Coordinate - paddle height); bottom
	if paddle_b.ycor() < (-300+50):
		paddle_b.sety(-300+50)
		
	
	#Paddle & ball collisions
	#b/w x=340-350, bounce ball back from paddle_b for all corresponding y-coordinates on paddle
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50): 
		ball.dx *= -1
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, 'bounce.wav')
		playsound(filename)
	
	#b/w x=-330-340, bounce ball back from paddle_a for all corresponding y-coordinates on paddle
	if (ball.xcor() < -330 and ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50): 
		ball.dx *= -1
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, 'bounce.wav')
		playsound(filename)
		

