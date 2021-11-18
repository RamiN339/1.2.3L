import turtle as trtl
import random
import time
import sys
#   a123_apple_1.py

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=600, height=400)
wn.addshape('pear.gif')
wn.addshape(apple_image) # Make the screen aware of the new file
pear = trtl.Turtle()
pear.ht()
apple = trtl.Turtle()
apple.ht()
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

applelist1 = [apple1, apple2, apple3, apple4, apple5, apple6]
for apples in applelist1:
  apples.pu()
  apples.ht()


drawer1 = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer4 = trtl.Turtle()
drawer5 = trtl.Turtle()
drawer6 = trtl.Turtle()
drawerlist = [drawer1, drawer2, drawer3, drawer4, drawer5, drawer6]
for drawerss in drawerlist:
  drawerss.ht()
letters=['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't','u', 'v', 'w','x','y','z']
turtle = apple
applelist = [apple1, apple2, apple3, apple4, apple5, apple6]

#-----functions-----
intspawn = 50

def applespawn(active_apple, x):
  for apples in applelist1:
    pearorapple=random.randint(0,1000)
    if apple.shape != 'pear.gif' or (apple_image):
      if pearorapple%2 ==0:
        apples.shape('pear.gif')
      else:
        apples.shape(apple_image)
  apple.pu()
  active_apple.shape(apple_image)
  apple.ht()
  xcors = []
  ycors=[]
  x1 = random.randint(-150,150)
  y1= random.randint(0,100)
  apple.ht()
  active_apple.clone().goto(x1,y1)
  apple.ht()
  xcors.append(x1)
  ycors.append(y1)
  for i in range(x):
      TrueCon = False
      TrueCony = False
      x1 = random.randint(-175,150)
      y1= random.randint(0,125) 
      for xvalues in xcors:
        if xvalues-40<x1<xvalues+40 or x1==xvalues:
          TrueCon = True
          break
      if TrueCon == False:
        xcors.append(x1)


      for yvalues in ycors:
        if yvalues-10<y1<yvalues+10 or y1==yvalues:
          TrueCony = True
          break
      if TrueCony == False:
        ycors.append(y1)



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
  print(len(xcors))
  for i in range(len(xcors)):
    print(i)
    try:
      if len (letters) != 1:
        print(xcors)
        print(ycors)
        print(letters)
        print(i)
        def drawletter(letter):
          drawer = drawerlist[i]
          draweruse.append(drawerlist[i])
          drawer.color('white')
          drawer.pu()
          drawer.goto(xcors[i]-10,ycors[i]-30)
          drawer.pd()
          drawer.write(letter, font=("Arial", 30, "bold"))
          drawer.pu()
          print('Drawer func Passed 🟢')
        print('Draw Set Passed 🟢')

        letterpickedr = random.randint(0,len(letters))
        letterpicked = letters[letterpickedr]
        letterused.append(letterpicked)
        letters.pop(letterpickedr)
        print('Letter Selection Passed 🟢')


        clonea = applelist[i]
        applesuse.append(applelist[i])
        clonea.st()
        clonea.goto(xcors[i], ycors[i])
        print('Turtle Moving Selection Passed 🟢')

        drawletter(letterpicked)
        print(str(clonea.xcor()) + ',' + str(clonea.ycor()))
        xcorgo.append(xcors[i])
        print('Check Passed 🟢🟢')
      else:
        winturtle = trtl.Turtle()
        wn.clear()
        winturtle.goto(-150,0)
        winturtle.pd()
        winturtle.write('You Won!', font=('Arial', 55, "bold"))
        time.sleep(3)
        sys.exit()
    except IndexError:
        print('err 🔴')

  global jeff
  def jeff():
      try:
        wn.onkeypress(applemove1,letterused[0])
      except Exception:
        asda='a'
      try:
        wn.onkeypress(applemove2,letterused[1])
      except Exception:
        asda='a'
      try:
        wn.onkeypress(applemove3,letterused[2])
      except Exception:
        asda='a'
      try:
        wn.onkeypress(applemove4,letterused[3])
      except Exception:
        asda='a'
      try:
        wn.onkeypress(applemove5,letterused[4])
      except Exception:
        asda='a'
      try:
        wn.onkeypress(applemove6,letterused[5])
      except Exception:
        asda='a'
  jeff()

def applemove1():
  try:
    draweruse[0].clear()
    applesuse[0].pu
    applesuse[0].goto(xcorgo[0], -150)
    applesuse[0].stamp()
    applesuse[0].ht()
    applesuse[0].goto(0,0)
    try:
      if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4].xcor() ==0 and applesuse[5].xcor() ==0:
        applespawn(turtle,intspawn)
    except Exception:
      try:
        if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4]:
          applespawn(turtle,intspawn)
      except Exception:
        try:
          if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0:
            applespawn(turtle, intspawn)
        except Exception:
          try:
            if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0:
              applespawn(turtle,intspawn)
          except Exception:
            try:
              if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0:
                applespawn(turtle,intspawn)
            except Exception:
              try:
                if applesuse[0].xcor() ==0:
                  applespawn(turtle,intspawn)
              except Exception:
                print('index out of range 🔴')
                print(applesuse)
  except IndexError:
    print('err2 🔴')



def applemove2():
  try:
    draweruse[1].clear()
    applesuse[1].pu
    applesuse[1].goto(xcorgo[1], -150)
    applesuse[1].stamp()
    applesuse[1].ht()
    applesuse[1].goto(0,0)
    try:
      if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4].xcor() ==0 and applesuse[5].xcor() ==0:
        applespawn(turtle,intspawn)
    except Exception:
      try:
        if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4]:
          applespawn(turtle,intspawn)
      except Exception:
        try:
          if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0:
            applespawn(turtle, intspawn)
        except Exception:
          try:
            if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0:
              applespawn(turtle,intspawn)
          except Exception:
            try:
              if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0:
                applespawn(turtle,intspawn)
            except Exception:
              try:
                if applesuse[0].xcor() ==0:
                  applespawn(turtle,intspawn)
              except Exception:
                print('index out of range 🔴')
                print(applesuse)
  except Exception:
    print('err2🔴')



def applemove3():
  try:
    draweruse[2].clear()
    applesuse[2].pu
    applesuse[2].goto(xcorgo[2], -150)
    applesuse[2].stamp()
    applesuse[2].ht()
    applesuse[2].goto(0,0)
    try:
      if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4].xcor() ==0 and applesuse[5].xcor() ==0:
        applespawn(turtle,intspawn)
    except Exception:
      try:
        if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4]:
          applespawn(turtle,intspawn)
      except Exception:
        try:
          if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0:
            applespawn(turtle, intspawn)
        except Exception:
          try:
            if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0:
              applespawn(turtle,intspawn)
          except Exception:
            try:
              if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0:
                applespawn(turtle,intspawn)
            except Exception:
              try:
                if applesuse[0].xcor() ==0:
                  applespawn(turtle,intspawn)
              except Exception:
                print('index out of range🔴')
                print(applesuse)
  except Exception:
    print('err2🔴')
    

def applemove4():
  try:
    draweruse[3].clear()
    applesuse[3].pu
    applesuse[3].goto(xcorgo[3], -150)
    applesuse[3].stamp()
    applesuse[3].ht()
    applesuse[3].goto(0,0)
    try:
      if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4].xcor() ==0 and applesuse[5].xcor() ==0:
        applespawn(turtle,intspawn)
    except Exception:
      try:
        if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4]:
          applespawn(turtle,intspawn)
      except Exception:
        try:
          if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0:
            applespawn(turtle, intspawn)
        except Exception:
          try:
            if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0:
              applespawn(turtle,intspawn)
          except Exception:
            try:
              if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0:
                applespawn(turtle,intspawn)
            except Exception:
              try:
                if applesuse[0].xcor() ==0:
                  applespawn(turtle,intspawn)
              except Exception:
                print('index out of range🔴')
                print(applesuse)
  except Exception:
    print('err2🔴')


def applemove5():
  try:
    draweruse[4].clear()
    applesuse[4].pu
    applesuse[4].goto(xcorgo[4], -150)
    applesuse[4].stamp()
    applesuse[4].ht()
    applesuse[4].goto(0,0)
    try:
      if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4].xcor() ==0 and applesuse[5].xcor() ==0:
        applespawn(turtle,intspawn)
    except Exception:
      try:
        if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4]:
          applespawn(turtle,intspawn)
      except Exception:
        try:
          if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0:
            applespawn(turtle, intspawn)
        except Exception:
          try:
            if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0:
              applespawn(turtle,intspawn)
          except Exception:
            try:
              if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0:
                applespawn(turtle,intspawn)
            except Exception:
              try:
                if applesuse[0].xcor() ==0:
                  applespawn(turtle,intspawn)
              except Exception:
                print('index out of range🔴')
                print(applesuse)
  except Exception:
    print('err2🔴')



def applemove6():
  try:
    draweruse[5].clear()
    applesuse[5].pu
    applesuse[5].goto(xcorgo[5], -150)
    applesuse[5].stamp()
    applesuse[5].ht()
    applesuse[5].goto(0,0)
    try:
      if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4].xcor() ==0 and applesuse[5].xcor() ==0:
        applespawn(turtle,intspawn)
    except Exception:
      try:
        if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0 and applesuse[4]:
          applespawn(turtle,intspawn)
      except Exception:
        try:
          if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0 and applesuse[3].xcor() ==0:
            applespawn(turtle, intspawn)
        except Exception:
          try:
            if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0 and applesuse[2].xcor() ==0:
              applespawn(turtle,intspawn)
          except Exception:
            try:
              if applesuse[0].xcor() == 0 and applesuse[1].xcor() ==0:
                applespawn(turtle,intspawn)
            except Exception:
              try:
                if applesuse[0].xcor() ==0:
                  applespawn(turtle,intspawn)
              except Exception:
                print('index out of range🔴')
                print(applesuse)
  except Exception:
    print('err2🔴')

#-----function calls-----
applespawn(turtle, intspawn)


wn.listen()
wn.mainloop()
