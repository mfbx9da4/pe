from math import sqrt

def main():
  n = 2
  nprimes = 0
  while True:
    prime = True
    for i in range(2,n):
      if n%i == 0:
        prime = False
        break
    if prime == True:
      nprimes+=1
      print nprimes, n
      if nprimes == 10001:
        break
    n+=1
  



if __name__ == "__main__":
    main()
