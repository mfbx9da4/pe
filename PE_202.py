from math import *
def calcangles(angle):
  angles=[angle]
  for i in range(20):
    angles.append(180-(angles[i]+60))
  print angles

angle = 45
origin = (0,0)
m = round(tan(radians(angle)),16)
y =1
x = y/m 
print m,x
