def tes (a):
  slice = a[0:len(a)-1]
  result = ''
  for val in reversed(slice):
    result += val
  print(a+result)

tes('procold')