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
def do_something_long():
  print("I'm feeling sleepy")
  time.sleep(5)
  
do_something_long()