# a) Hàm tính tổng các chữ số của n
def tong_chu_so(n):
    return sum(int(digit) for digit in str(n))

# b) Hàm kiểm tra số Armstrong
def la_armstrong(n):
    s = str(n)
    k = len(s)
    tong_luy_thua = sum(int(digit)**k for digit in s)
    return tong_luy_thua == n

# d) Hàm kiểm tra số hoàn hảo (Số có tổng các ước thực sự bằng chính nó)
def la_so_hoan_hao(n):
    if n < 2: return False
    # Tìm các ước thực sự (không bao gồm n)
    tong_uoc = sum(i for i in range(1, n) if n % i == 0)
    return tong_uoc == n

# Thực thi chương trình theo yêu cầu ví dụ
if __name__ == "__main__":
    # Nhập n từ bàn phím
    n_input = int(input("Nhap n: "))

    # a) In tổng chữ số
    print(f"Tong chu so cua {n_input} = {tong_chu_so(n_input)}")

    # b) Kiểm tra số Armstrong cho số vừa nhập
    if la_armstrong(n_input):
        print(f"{n_input} LA so Armstrong!")
    else:
        print(f"{n_input} KHONG LA so Armstrong!")

    # c) In tất cả số Armstrong có 3 chữ số (100-999)
    armstrong_3_chu_so = [i for i in range(100, 1000) if la_armstrong(i)]
    print(f"So Armstrong 3 chu so: {armstrong_3_chu_so}")

    # d) In số hoàn hảo từ 1 đến 1000
    so_hoan_hao_list = [i for i in range(1, 1001) if la_so_hoan_hao(i)]
    print(f"So hoan hao tu 1-1000: {so_hoan_hao_list}")
