import turtle as trtl
import random

#   a123_apple_1.py

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape('pear.gif')
wn.addshape(apple_image) # Make the screen aware of the new file
pear = trtl.Turtle()
apple = trtl.Turtle()
wn.bgpic('background.gif')
drawer = trtl.Turtle()
drawer.ht()
apple.shape(apple_image)
apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()
apple6 = trtl.Turtle()
apple1.ht()
apple2.ht()
apple3.ht()
apple4.ht()
apple5.ht()
apple6.ht()
apple1.pu()
apple2.pu()
apple3.pu()
apple4.pu()
apple5.pu()
apple6.pu()
apple1.shape(apple_image)
apple2.shape(apple_image)
apple3.shape(apple_image)
apple4.shape(apple_image)
apple5.shape(apple_image)
apple6.shape(apple_image)
drawer1 = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer4 = trtl.Turtle()
drawer5 = trtl.Turtle()
drawer6 = trtl.Turtle()
drawer1.ht()
drawer2.ht()
drawer3.ht()
drawer4.ht()
drawer5.ht()
drawer6.ht()
drawerlist = [drawer1, drawer2, drawer3, drawer4, drawer5, drawer6]
letters=['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s']
turtle = apple
applelist = [apple1, apple2, apple3, apple4, apple5, apple6]
#-----functions-----
intspawn = random.randint(3,15)

def applespawn(active_apple, x):
  apple.pu()
  active_apple.shape(apple_image)
  apple.ht()
  print('hai')
  xcors = []
  ycors=[]
  x1 = random.randint(-150,150)
  y1= random.randint(0,100)
  apple.ht()
  active_apple.clone().goto(x1,y1)
  apple.ht()
  xcors.append(x1)
  ycors.append(y1)
  print(x1)
  print(y1)
  for i in range(x):
      TrueCon = False
      TrueCony = False
      print(i)
      x1 = random.randint(-150,150)
      y1= random.randint(0,100) 
      for xvalues in xcors:
        print( xcors)
        print('x1: ' + str(x1))
        print('Xvalues: '+ str(xvalues))
        if xvalues-45<x1<xvalues+45 or x1==xvalues:
          print('hi')
          TrueCon = True
          break
      if TrueCon == False:
        print(x1)
        xcors.append(x1)


      for yvalues in ycors:
        print(ycors)
        print('y1: ' + str(y1))
        print('yvalues: '+ str(yvalues))
        if yvalues-10<y1<yvalues+10 or y1==yvalues:
          print('hi')
          TrueCony = True
          break
      if TrueCony == False:
        print(y1)
        ycors.append(y1)


  print(xcors)
  print(ycors)
  xcors.pop(0)
  ycors.pop(0)
  global applesuse
  applesuse=[]
  global letterused
  letterused =[]
  global draweruse
  draweruse = []
  global xcorgo
  xcorgo=[]
  for i in range(len(xcors)):
    try:
      def drawletter(letter):
        drawer = drawerlist[i]
        draweruse.append(drawerlist[i])
        print(drawer)
        drawer.color('white')
        drawer.pu()
        drawer.goto(xcors[i]-10,ycors[i]-30)
        drawer.pd()
        drawer.write(letter, font=("Arial", 30, "bold"))
        drawer.pu()
      letterpickedr = random.randint(0,18)
      letterpicked = letters[letterpickedr]
      letterused.append(letterpicked)
      letters.pop(letterpickedr)

      clonea = applelist[i]
      applesuse.append(applelist[i])
      clonea.st()
      #applelist.pop(i)
      clonea.goto(xcors[i], ycors[i])
      drawletter(letterpicked)
      print(str(clonea.xcor()) + ',' + str(clonea.ycor()))
      xcorgo.append(xcors[i])
    except IndexError:
      continue


def applemove1():
  try:
    draweruse[0].clear()
    applesuse[0].pu
    applesuse[0].goto(xcorgo[0], -150)
  except Exception:
    print('index out of range')

def applemove2():
  try:
    draweruse[1].clear()
    applesuse[1].pu
    applesuse[1].goto(xcorgo[1], -150)
    
  except Exception:
    print('index out of range')

def applemove3():
  try:
    draweruse[2].clear()
    applesuse[2].pu
    applesuse[2].goto(xcorgo[2], -150)
    
  except Exception:
    print('index out of range')
    

def applemove4():
  try:
    draweruse[3].clear()
    applesuse[3].pu
    applesuse[3].goto(xcorgo[3], -150)
    
  except Exception:
    print('index out of range')

def applemove5():
  try:
    draweruse[4].clear()
    applesuse[4].pu
    applesuse[4].goto(xcorgo[4], -150)
  except Exception:
    print('index out of range')

def applemove6():
  try:
    draweruse[5].clear()
    applesuse[5].pu
    applesuse[5].goto(xcorgo[5], -150)
  except Exception:
    print('index out of range')


#-----function calls-----
applespawn(turtle, intspawn)
import time
time.sleep(1)
wn.onkeypress(applemove1,letterused[0])
try:
  wn.onkeypress(applemove2,letterused[1])
except:
  print('o')
try:
  wn.onkeypress(applemove3,letterused[2])
except:
  print('o')
try:
  wn.onkeypress(applemove4,letterused[3])
except:
  print('o')
try:
  wn.onkeypress(applemove5,letterused[4])
except:
  print('o')
try:
  wn.onkeypress(applemove6,letterused[5])
except:
  print('o')
print(applelist)
wn.listen()
wn.mainloop()
