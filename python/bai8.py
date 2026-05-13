# Chương trình giải phương trình bậc hai ax^2 + bx + c = 0

import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -c / b
        print("Phuong trinh co nghiem x =", x)

else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("Delta =", delta, "> 0")
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2*a)

        print("Delta = 0")
        print("Nghiem kep x =", x)

    else:
        print("Delta <", 0)
        print("Phuong trinh vo nghiem")