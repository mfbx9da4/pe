from termcolor import *
import re
from numpy import *

def printcolored(l):
  y = linspace(0,100,9)
  clrs = ['grey','red','green','yellow','blue','magenta','cyan','white']
  l = array(map(int,l))
  #print l
  for x in l:
    for i in range(len(clrs)):
      if x>=y[i] and x<y[i+1]:
        print colored('  ',clrs[i],str('on_'+clrs[i])),
        break
  print str(str(average(l))+' '+str(std(l))).rjust(80)

f = open('triangle .txt','r+b')
rows = map(lambda x: re.findall('\d\d',x), f.readlines())
#for x in rows: print x
for i in range(len(rows)): printcolored(rows[i])
