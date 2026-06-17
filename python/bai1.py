

gio_hang = []

# a
gio_hang.append(("Áo polo", 299000))
gio_hang.append(("Quần jeans", 599000))
gio_hang.append(("Giày", 899000))
gio_hang.append(("Mũ", 149000))
gio_hang.append(("Tất", 49000))

# b) 
tong = 0
for sp in gio_hang:
    tong += sp[1]

print("Tong gia tri gio hang:", tong)

# c) 
for sp in gio_hang:
    if sp[0] == "Mũ":
        gio_hang.remove(sp)
        break

# d) 
gio_hang.sort(key=lambda x: x[1])

print("\nDanh sach san pham sau khi sap xep:")
for ten, gia in gio_hang:
    print(ten, "-", gia)

# e) 
print("\nSan pham re nhat:", gio_hang[0])
print("San pham dat nhat:", gio_hang[-1])