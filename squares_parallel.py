import multiprocessing
import time

def compute_squares(number):
  return number ** 2

# Python idiom - the code below will not get run if you import the module
if __name__ == '__main__': 
  pool = multiprocessing.Pool(20)
  result = pool.map(compute_squares, range(1000))
  print(result)
