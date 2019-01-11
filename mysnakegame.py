import turtle
import time
import random

delay=0.1
score=0
high_score=0


wn=turtle.Screen()
wn.title("Snake game by Arpit")
wn.bgcolor("pink")
wn.setup(width=600 , height=600)
wn.tracer(0) #turns off animation

#snake head
head=turtle.Turtle()
head.speed(0) #fastest speed possible
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake food
food=turtle.Turtle()
food.speed(0) #fastest speed possible
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

#blockage
block=turtle.Turtle()
block.speed(0)
block.shape("triangle")
block.color("yellow")
block.penup()
block.resizemode("user")
block.shapesize(2, 2,8)
x_block=random.randint(-250,250)
y_block=random.randint(-250,250)
if (x_block!= food.xcor and y_block != food.ycor):
    block.goto(x_block,y_block)
else:
    x_b2=random.randint(-250,250)
    y_b2=random.randint(-250,250)
    block.goto(x_b2,y_b2)
    
    

#block2
block2=turtle.Turtle()
block2.speed(0)
block2.shape("circle")
block2.color("cyan")
block2.penup()
block2.resizemode("user")
block2.shapesize(4,4,8)
x_block2= random.randint(-240,240)
y_block2=random.randint(-240,240)
block2.goto(x_block2,y_block2)

#movingobjects
mb=turtle.Turtle()
mb.speed(0) #fastest speed possible
mb.shape("circle")
mb.color("orange")
mb.penup()
mb.goto(0,250)
mb.direction="stop"

segments=[]

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score :0 High Score : 0",align ="center" ,font=("Courier" ,24 ,"normal"))

def go_up():
    if head.direction != "down":
        head.direction ="up"

def go_down():
    if head.direction != "up":
        head.direction ="down"
    
def go_left():
    if head.direction != "right":
        head.direction ="left"
    
def go_right():
    if head.direction != "left":
        head.direction ="right"

#Functions
def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y= head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x= head.xcor()
        head.setx(x+20)
        
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#Main game loop
while True:
    wn.update()
    #colllision with blocks
    if head.distance(block)<35:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
        
            #clear the segments list
            segments.clear()
            
            #reset the delay
            delay=0.1
            #rest the new position of block
            x_blockreset=random.randint(-250,250)
            y_blockreset=random.randint(-250,250)
            block.goto(x_blockreset,y_blockreset)
            
            score=0
            pen.clear()
            pen.write("Score :{} High Score : {}".format(score,high_score),align="center" ,font=("Courier" ,24 ,"normal"))
    
    #check for collision with circular block
    if head.distance(block2)<35:
        if delay>0:
            delay-=0.005
            x_blockcircle=random.randint(-250,250)
            y_blockcircle=random.randint(-250,250)
            block2.goto(x_blockcircle,y_blockcircle)
            
    
    #Check for a collision with borders
    if head.xcor()>290 or head.xcor() <-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        
        #clear the segments list
        segments.clear()
        
        #Resets the Score
        score=0
        
        #reset the delay
        delay=0.1
            
        pen.clear()
        pen.write("Score :{} High Score : {}".format(score,high_score),align="center" ,font=("Courier" ,24 ,"normal"))
    # Check for a collision with the food
    if head.distance(food)<20 :
        #Move the food to a random spot
        x= random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0) #fastest speed possible
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.goto(0,100)
        segments.append(new_segment)
        
        #reset the delay
        delay -=0.001
        
        score+=10
        if score > high_score:
            high_score=score
            
        pen.clear()
        pen.write("Score :{} High Score : {}".format(score,high_score),align="center" ,font=("Courier" ,24 ,"normal"))
    
    #move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where head is 
    if len(segments) > 0 :
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        
    move()
    
    #check for collision with the body
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
        
            #clear the segments list
            segments.clear()
            
            #reset the delay
            delay=0.1
            
            score=0
            pen.clear()
            pen.write("Score :{} High Score : {}".format(score,high_score),align="center" ,font=("Courier" ,24 ,"normal"))
            
    #moving object
    y=mb.ycor()
    mb.sety(y-8)
    
    if y<-290:
        x= random.randint(-280,280)
        y=290
        mb.goto(x,y)
    
    
            
    time.sleep(delay)

wn.mainloop() #keeps the window open