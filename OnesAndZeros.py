#change array of 0s and 1s (binary) into decimal

def binary_array_to_number(arr):
  size = len(arr) -1
  spot = 0
  number = 0
  while size >= 0:
    if arr[size] > 0:
      number = number + (2**spot)
    size = size - 1
    spot = spot + 1
  return number