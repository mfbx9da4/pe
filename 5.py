from math import sqrt

def main():
  i = 1
  while True:
    ed = 0
    skip = False
    for x in range(1,21):
      if (i)%x == 0:
        ed+=1
      #print i, '%',x,'=',(i)%x,'==>',ed
    if ed == 20:
      print i
      break
    i+=1



if __name__ == "__main__":
    main()
