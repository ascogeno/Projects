def euclid(x, y):
    """
    Implements the euclid algorithm to find the GCD
    of x and y in linear combination form. This
    function returns a tuple (gcd, s, t) where
    gcd = s*x + t*y.
    """
    if x == 0:
        return (y, 0, 1)
    (gcd, s, t) = euclid(y % x, x)
    return (gcd, t - (y // x) * s, s)

def manual_euclid(x, y, s0=1, t0=0, s1=0, t1=1, c=1):
    if x == 0:
        print(f"row {c}")
        print(f"x = {x}")
        print(f"y = {y}")
        print(f"r = -")
        print(f"q = -")
        print(f"s = {s1}")
        print(f"t = {t1}")
        print()
        return

    r = y % x
    q = y // x
 
    print(f"row {c}")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"r = {r}")
    print(f"q = {q}")
    print(f"s = {s0}")
    print(f"t = {t0}")
    print()

    s_next = s0 - q * s1
    t_next = t0 - q * t1

    manual_euclid(r, x, s1, t1, s_next, t_next, c + 1)



x = 43
y = 57
r = y%x
q = y//x
s = 1
t = 0
counter = 1

manual_euclid(x,y)
#print(euclid(x, y))