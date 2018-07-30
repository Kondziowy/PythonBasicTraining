import multiprocessing
import time
from functools import wraps

def logging_decorator(f):
  @wraps(f)
  def wrapper(*args, **kwds):
    print('Entering decorator')
    result=f(*args, **kwds)
    print('Exiting decorator')
    return result
  return wrapper

@logging_decorator
def compute_squares(number):
  return number ** 2

if __name__ == '__main__':
  pool = multiprocessing.Pool(20)
  result = pool.map(compute_squares, range(1000))
  print(result)