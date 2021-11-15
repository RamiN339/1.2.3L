import turtle as trtl
import random
#   a123_apple_1.py

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
intspawn = 4 #random.randint(1,4)
print(intspawn)
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape('pear.gif')
wn.addshape(apple_image) # Make the screen aware of the new file
pear = trtl.Turtle()
apple = trtl.Turtle()
wn.bgpic('background.gif')

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.ht()
  active_pear.shape('pear.gif')
  wn.update()

def applespawn(active_apple, x):
  loopstart = 0
  ycors = []
  xcors=[]
  while loopstart < x:
    loopstart += 1
    global checkfory
    checkfory = False
    global checkforx
    checkforx = False
    active_apple.st()
    active_apple.shape(apple_image)
    active_apple.pu()
    active_apple.speed(0)
    global appletomove
    ypostospawn = random.randint(0,100)
    xpostospawn = random.randint(-150,150)
    appletomove = active_apple.clone()
    active_apple.hideturtle()
    if len(ycors) >= 1:
      for yvalues in ycors:
        if yvalues-50<ypostospawn <yvalues+50:
          continue
        else:
          checkfory = True
      for xvalues in xcors:
        if xvalues-50<xpostospawn <xvalues+50:
          continue
        else:
              checkforx = True
    else:
      print('asd')
      appletomove.goto(xpostospawn, ypostospawn)
      prevxpos =appletomove.xcor()
      prevypos = appletomove.ycor()
      xcors.append(prevxpos)
      ycors.append(prevypos)
    if checkfory == True and checkforx == True:
              appletomove.goto(xpostospawn, ypostospawn)
              print(appletomove.xcor(), appletomove.ycor())
              prevxpos =appletomove.xcor()
              prevypos = appletomove.ycor()
              xcors.append(prevxpos)
              ycors.append(prevypos)
              print(xcors)
              print(ycors)
      




#-----function calls-----
draw_pear(pear)
applespawn(apple, intspawn)
wn.mainloop()