# Chương trình đổi số thập phân sang:
# - Hệ nhị phân
# - Hệ bát phân
# - Hệ thập lục phân
# bằng vòng lặp while

n = int(input("Nhap n: "))


tam = n
nhi_phan = ""

if tam == 0:
    nhi_phan = "0"

while tam > 0:
    du = tam % 2
    nhi_phan = str(du) + nhi_phan
    tam //= 2



tam = n
bat_phan = ""

if tam == 0:
    bat_phan = "0"

while tam > 0:
    du = tam % 8
    bat_phan = str(du) + bat_phan
    tam //= 8



tam = n
thap_luc_phan = ""
ky_tu = "0123456789ABCDEF"

if tam == 0:
    thap_luc_phan = "0"

while tam > 0:
    du = tam % 16
    thap_luc_phan = ky_tu[du] + thap_luc_phan
    tam //= 16



print(n, "(thap phan) =", nhi_phan, "(nhi phan)")
print(n, "(thap phan) =", bat_phan, "(bat phan)")
print(n, "(thap phan) =", thap_luc_phan, "(thap luc phan)")