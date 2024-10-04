import math

a = int(input("Nilai A: "))
b = int(input("Nilai B: "))
c = int(input("Nilai C: "))

diskriminan = (b**2) - (4*a*c)

print("persamaan kuadrat:", a, "x2 +", b, "x +", c)
print("Diskriminan:", diskriminan)

if diskriminan == 0:
    x = -b / (2*a)
    print("Merupakan akar kembar")
    print("akar =", x)
elif diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print("Merupakan akar berbeda")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("Merupakan akar imajiner")
    print("x1 =", (-b + cmath.sqrt(diskriminan)) / (2 * a))
    print("x2 =", (-b - cmath.sqrt(diskriminan)) / (2 * a))