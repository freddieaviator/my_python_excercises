def next_collatz_element(n):
  lst=[]
  lst.append(n)
  while(n!=1):
      if(n%2==0):
          n=n//2
          lst.append(n)
      else:
          n=n*3+1
          lst.append(n)
  return lst

print(next_collatz_element(2))