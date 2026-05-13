# Chương trình kiểm tra số nguyên tố

import math

n = int(input("Nhap n: "))

if n < 2:
    print(n, "khong phai la so nguyen to")
else:
    la_snt = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            la_snt = False
            break

    if la_snt:
        print(n, "la so nguyen to")
    else:
        print(n, "khong phai la so nguyen to")