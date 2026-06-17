

lich_su_mua = ["SP001", "SP003", "SP005", "SP002", "SP003"]

san_pham = [
    ("SP001", "Áo polo", 299000),
    ("SP002", "Quần", 599000),
    ("SP003", "Giày", 899000),
    ("SP004", "Mũ", 149000),
    ("SP005", "Tất", 49000)
]

# a) 

sp_mua_nhieu_nhat = ""
so_lan_max = 0

for ma_sp in lich_su_mua:
    if lich_su_mua.count(ma_sp) > so_lan_max:
        so_lan_max = lich_su_mua.count(ma_sp)
        sp_mua_nhieu_nhat = ma_sp

print("San pham duoc mua nhieu nhat:", sp_mua_nhieu_nhat)
print("So lan mua:", so_lan_max)

# b) 

sp_chua_mua = [sp for sp in san_pham if sp[0] not in lich_su_mua]

print("\nSan pham chua duoc mua:")
for sp in sp_chua_mua:
    print(sp)

# c) 

tong_chi_tieu = 0

for ma_sp in lich_su_mua:
    for thong_tin_sp in san_pham:
        if ma_sp == thong_tin_sp[0]:
            tong_chi_tieu += thong_tin_sp[2]

print("\nTong chi tieu cua khach hang:", tong_chi_tieu)