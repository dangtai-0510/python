# Chương trình in n số đầu tiên của dãy Fibonacci

n = int(input("Nhap n: "))

a = 1
b = 1

print("Day Fibonacci:")

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c