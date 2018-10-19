#Returns the amount of values that are multiples or 3 or 5
#that are under or equal to the entered number

def solution(number):
  solution = 0
  counter = 0
  while counter < number:
      if counter%3 == 0 or counter%5 == 0:
          solution += counter
      counter += 1
  return solution