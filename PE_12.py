from numpy import array, arange
from termcolor import *
from math import sqrt

def trinum(n):
  return sum(xrange(n))
def ndivisors(n):
  count = list(n%arange(1,int(sqrt(n)))).count(0)*2
  if sqrt(n)-int(sqrt(n)) ==0.0: return count-1
  else: return count

topnd,nd,i=0,0,0
while nd <=500:
  n=trinum(i+1)
  nd=ndivisors(n)
  if nd>topnd: 
    topnd = nd
    print i,n,nd
  i+=1
