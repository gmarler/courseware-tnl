def add(increment):
  def decorator(func):
    def wrapper(*args, **kwargs):
      return increment + func(*args, **kwargs)
    return wrapper
  return decorator

def multiply(multiplier):
  def decorator(func):
    def wrapper(*args, **kwargs):
      return multiplier * func(*args, **kwargs)
    return wrapper
  return decorator


@add(3)
def f(n):
  return n + 2

print(f(4))

@multiply(2)
@add(3)
def g(n):
  return n + 2

print(g(4))
