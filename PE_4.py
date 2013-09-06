from math import sqrt

def main():
  pallindrome = 0
  for i in range(999):
    for j in range(999):
      prod = str(i*j)
      inv = ''
      for x in range(len(prod)):
        inv += prod[-(x+1)]
      if prod == inv:
        #print prod
        if i*j > pallindrome:
          pallindrome = i*j
  print pallindrome
  
  
  
if __name__ == "__main__":
    main()
