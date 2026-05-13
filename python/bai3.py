# Chương trình tính tổng, tổng chẵn và tổng lẻ từ 1 đến n

n = int(input("Nhap n: "))

tong = 0
tong_chan = 0
tong_le = 0

for i in range(1, n + 1):
    tong += i

    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print("Tong S =", tong)
print("Tong chan =", tong_chan)
print("Tong le =", tong_le)