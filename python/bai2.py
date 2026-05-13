# Chương trình xếp loại học sinh theo điểm trung bình

dtb = float(input("Nhap diem trung binh: "))

if dtb < 0 or dtb > 10:
    print("Diem khong hop le!")
elif dtb >= 9.0:
    print("Xep loai: Xuat sac")
elif dtb >= 8.0:
    print("Xep loai: Gioi")
elif dtb >= 7.0:
    print("Xep loai: Kha")
elif dtb >= 6.5:
    print("Xep loai: Trung binh kha")
elif dtb >= 5.0:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")