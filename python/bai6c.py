# Chương trình tìm số Fibonacci đầu tiên lớn hơn 1000

a = 1
b = 1

while a <= 1000:
    c = a + b
    a = b
    b = c

print("So Fibonacci dau tien lon hon 1000 la:", a)