from math import sqrt

def main():
  #sumsq = (((1/3)*(100**3)) + ((1/2)*(100**2)) + (1/6)*100)
  sumsq = sum([ n**2 for n in range(1,101)])
  sqsum = sum(range(1,101))**2
  print sqsum-sumsq



if __name__ == "__main__":
    main()
