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
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.ht()
  active_pear.shape('pear.gif')
  wn.update()

def drawletter(letter):
  drawer.color('white')
  drawer.pu()
  drawer.goto(apple.xcor()-10,apple.ycor()-30)
  drawer.pd()
  drawer.write(letter, font=("Arial", 30, "bold"))
  
def applespawn():
  drawer.clear()
  active_apple = apple
  active_apple.pu()
  active_apple.goto(0, -150)



      
    



#-----function calls-----
draw_pear(pear)
drawletter('a')
wn.onkeypress(applespawn, 'a')
wn.listen()
wn.mainloop()
