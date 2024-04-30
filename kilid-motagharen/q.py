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

def calculate_curve_slope(xp, yp, xq, yq, a, p):
    s = 0
    if xp != xq or yp != yq:
        s = ((yq - yp) * mod_inverse(xq - xp, p)) % p
    else:
        s = ((3*(xp**2) + a) * mod_inverse(2*yp, p)) % p
    return s
    
def elliptic_sum(a, b, p, xp, yp, xq, yq):
    if xp == None and yp == None:
        return (xq, yq) 
    elif xq == None and yq == None:
        return (xp, yp)

    s = calculate_curve_slope(xp, yp, xq, yq, a, p)
    
    xr = (s**2 - xp - xq) % p
    yr = -(yp - (s * (xp - xr))) % p
    
    return (xr, yr)


def elliptic_multiply(a, b, p, x, y, k):
    r = (None, None)
    powerer = (x, y)
    while k != 0:
        if k & 1:
            # print(r)
            r = elliptic_sum(a, b, p, r[0], r[1], powerer[0], powerer[1])
        powerer = elliptic_sum(a, b, p, powerer[0], powerer[1], powerer[0], powerer[1])
        k >>= 1
            
    # this did not work :/
    # for _ in range(k - 1):
    #     print(r)
    #     r = elliptic_sum(a, b, p, r[0], r[1], x, y)     
       
    return r

################################################################## main
if __name__ == '__main__':
    p = int(input())    # p: encryption property       P: piont on curve
    a = int(input())
    b = int(input())
    xg = int(input())
    yg = int(input())
    x = int(input())
    y = int(input())

    if not is_prime(p):
        print("p is not prime")
    elif not is_k_on_curve(a, b, p, xg, yg):
        print("G is not on the curve")
    else:
        # if x >= y:
        #     x, y = y, x
        r = elliptic_multiply(a, b, p, xg, yg, x)
        r = elliptic_multiply(a, b, p, r[0], r[1], y)

        # this did not work also :///
        # r = elliptic_multiply(a, b, p, xg, yg, y)
        # r = elliptic_multiply(a, b, p, r[0], r[1], x)

        print(str(r[0]) + str(r[1]))