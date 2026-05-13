# Chương trình tính UCLN và BCNN bằng thuật toán Euclid

def ucln(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def bcnn(a, b):
    return a * b // ucln(a, b)

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("UCLN(", a, ",", b, ") =", ucln(a, b))
print("BCNN(", a, ",", b, ") =", bcnn(a, b))