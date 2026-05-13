# Chương trình kiểm tra một số có thuộc dãy Fibonacci không

n = int(input("Nhap n: "))

a = 1
b = 1

while a < n:
    c = a + b
    a = b
    b = c

if a == n:
    print(n, "co trong day Fibonacci")
else:
    print(n, "khong co trong day Fibonacci")