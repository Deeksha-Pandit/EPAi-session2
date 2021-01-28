import time
import math

def time_it(fn, *args, repetitons= 1, **kwargs):
  if repetitons < 1:
    raise ValueError("Cannot have negative repetitions!!!")
  start1 = time.perf_counter()
  for i in range(repetitons):
    fn(*args, **kwargs)
  end1 = time.perf_counter()
  delta1 = end1 - start1
  return (delta1/repetitons)

def print_func(*args,**kwargs):
    print(*args,**kwargs)

def squared_power_list(num, start=0, end=5):
  l = []
  if start < 0:
    raise ValueError("Cannot have negative values as power")
  for i in range(start, end+1):
    res = num ** start
    l.append(res)
  return l

def polygon_area(len, sides):
  if sides < 3 or sides > 6:
    raise ValueError("Number of side must be between 3 and 6")
  if len < 0:
    raise ValueError("Length of side must be positive")
  return sides * (len**2) / (4 * math.tan(math.pi/sides))

def temp_converter(temp, temp_given_in):
    if temp_given_in  not in ('f', 'c'):
        raise ValueError('Temperature must only be specified as "f" or "c"')
    if temp_given_in == 'f':
        return ((temp-32) * (5/9))
    else:
        return ((temp * 9/5) + 32)

def speed_converter(speed=100, dist='km', time='min'):
    if speed < 0:
        raise ValueError('Speed cannot be lesser than zero')
    if dist == 'km':
        speed *= 1
    elif dist == 'm':
        speed *= 1000
    elif dist == 'ft':
        speed *= 3280.84
    elif dist == 'yrd':
        speed *= 1093.61

    if time == 'hr':
        speed /= 1
    elif time == 'm':
        speed /= 60
    elif time == 's':
        speed /= 3600
    elif time == 'ms':
        speed /= 3600000
    elif time == 'day':
        speed *= 24

    return speed


