
def main():
  i = 0
  x = 0
  fs = [1,2]
  while x < 4000000:
    x = fs[i]+fs[i+1]
    fs.append(x)
    i+=1
  del fs[-1]
  print fs
  
  fseven = []
  for x in fs:
    if not x % 2:
      fseven.append(x)
  print fseven
  print sum(fseven)
  
  
  
if __name__ == "__main__":
    main()
