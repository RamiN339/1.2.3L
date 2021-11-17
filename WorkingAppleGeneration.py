intspawn = random.randint(1,10)

def applespawn(active_apple, x):
  apple.pu()
  active_apple.shape(apple_image)
  apple.ht()
  print('hai')
  xcors = []
  ycors=[]
  x1 = random.randint(-150,150)
  y1= random.randint(0,100)
  apple.st()
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
        if xvalues-50<x1<xvalues+50 or x1==xvalues:
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
  for i in range(len(xcors)):
    try:
      active_apple.st()
      clonea = active_apple.clone()
      clonea.goto(xcors[i], ycors[i])
      print(str(clonea.xcor()) + ',' + str(clonea.ycor()))
      active_apple.ht()
    except IndexError:
      continue
  applespawn(turtle, intspawn)

