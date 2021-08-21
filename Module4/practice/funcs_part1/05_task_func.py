def m (xa, ya, xb, yb, xc, yc):
    a = m((xb-xa)**2 +(yb - ya)**2)**0.5
    b = m((xc-xa)**2 +(yc - ya)**2)**0.5
    c = m((xc-xb)**2 +(xc - xb)**2)**0.5
    p = m(a + b + c) / 2
    if a + b > c and b + c > a and a + c > b:
        return a + b > c and b + c > a and a + c > b
    else:
        print("треугольник построить нельзя")
def s(xa, ya, xb, yb, xc, yc):
    return (p(p - a)(p - b)(p - c)) ** 0.5

def per(xa, ya, xb, yb, xc, yc):
    return a + b + c
