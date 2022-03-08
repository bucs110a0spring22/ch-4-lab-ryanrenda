import turtle
import math

def drawSineCurve(dart):
  for i in range(0, 721):
    y = math.sin(math.radians(i-360))
    x = math.radians(i-360)
    dart.goto(x, y)
  dart.up()

def setupWindow(wn):
  wn.setworldcoordinates(-2*math.pi, -1, 2*math.pi, 1)
  wn.bgcolor("lightblue")
  
def setupAxis(dart):
  dart.up()
  dart.goto(0, 1)
  dart.down()
  dart.goto(0, -1)
  dart.up()
  dart.goto(2*math.pi, 0)
  dart.down()
  dart.goto(-2*math.pi, 0)

def drawCosineCurve(dart):
  dart.goto(-2*math.pi, 1)
  dart.down()
  for i in range(0, 721):
    y = math.cos(math.radians(i-360))
    x = math.radians(i-360)
    dart.goto(x, y)
  dart.up()
  
def drawTangentCurve(dart):
  dart.goto(-2*math.pi, 0)
  dart.down()
  for i in range(0, 721):
    y = math.tan(math.radians(i-360))
    x = math.radians(i-360)
    dart.goto(x, y)

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
