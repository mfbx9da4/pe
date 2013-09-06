from math import sqrt

def main():
  i = 1
  multiples = []
  while 3*i < 1000:
    multiples.append(3*i)
    i+=1
  i = 1
  while 5*i < 1000:
    if 5*i not in multiples:
      multiples.append(5*i)
    i+=1
  multiples = sorted(multiples)
  print multiples
  print sum(multiples)
  
  
  
if __name__ == "__main__":
    main()
