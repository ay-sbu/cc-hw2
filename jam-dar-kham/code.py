import math

################################################################## functions
def mod_inverse(n: int, mod: int):
    return pow(n, -1, mod)

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6

  return True   

def is_k_on_curve(a, b, p, x, y):
    return (y**2) % p == (x**3 + a*x + b) % p

def calculate_curve_slope(xp, yp, xq, yq, a):
    s = 0
    if xp != xq or yp != yq:
        s = ((yq - yp) * mod_inverse(xq - xp, p)) % p
    else:
        s = ((3*(xp**2) + a) * mod_inverse(2*yp, p)) % p
    return s
    
def calculate_r(a, b, p, xp, yp, xq, yq):
    s = calculate_curve_slope(xp, yp, xq, yq, a)
    
    xr = (s**2 - xp - xq) % p
    yr = -(yp - (s * (xp - xr))) % p
    
    return (xr, yr)

################################################################## main
p = int(input())    # p: encryption property       P: piont on curve
a = int(input())
b = int(input())
xp = int(input())
yp = int(input())
xq = int(input())
yq = int(input())

if not is_prime(p):
    print("p is not prime")
elif not is_k_on_curve(a, b, p, xp, yp):
    print("P is not on the curve")
elif not is_k_on_curve(a, b, p, xq, yq):
    print("Q is not on the curve")
else:
    r = calculate_r(a, b, p, xp, yp, xq, yq)
    print(r)