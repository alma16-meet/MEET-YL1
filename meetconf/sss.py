
import turtle



#triangle


def make_a_triangle (x,y):


    turtle.penup()
    turtle.goto(x+20,y+20)
    turtle.pendown()
    turtle.goto(x+40,y+20)
    turtle.goto(x+30,y+40)
    turtle.goto(x+20,y+20)
    turtle.pendown()

    
make_a_triangle(0,0)

#square

def make_a_square (x,y):

  turtle.penup()
  turtle.goto(x+60,y+60)
  turtle.pendown()
  turtle.goto(x+60,y+100)
  turtle.goto(x+100,y+100)
  turtle.goto(x+100,y+60)
  turtle.goto(x+60,y+60)


make_a_square(0,0)

#click to draw square

turtle.onscreenclick(make_a_square,btn=1,add=True)


#click to draw triangle

turtle.onscreenclick(make_a_triangle,btn=3,add=True)

#Blue

def blue():
    turtle.color("blue")

#switch to blue
turtle.getscreen().onkeypress(blue,"b")
turtle.getscreen().listen

#Red

def red():
    turtle.color("red")

#switch to red
turtle.getscreen().onkeypress(red,"r")
turtle.getscreen().listen


















    
