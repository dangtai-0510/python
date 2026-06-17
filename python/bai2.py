

ds_dt = [125.5, 98.2, 145.8, 110.3, 168.0, 132.7,
         155.4, 89.6, 178.2, 143.1, 160.0, 121.8]

# a) 
dt_max = max(ds_dt)
dt_min = min(ds_dt)

thang_max = ds_dt.index(dt_max) + 1
thang_min = ds_dt.index(dt_min) + 1

print("Doanh thu cao nhat:", dt_max, "- Thang", thang_max)
print("Doanh thu thap nhat:", dt_min, "- Thang", thang_min)

# b) 
tong = sum(ds_dt)
tb = tong / len(ds_dt)

print("Tong doanh thu:", tong)
print("Trung binh doanh thu:", round(tb, 2))

# c) 
count = 0

for dt in ds_dt:
    if dt > tb:
        count += 1

print("So thang cao hon trung binh:", count)

# d) 
ds_quy = [sum(ds_dt[i:i+3]) for i in range(0, len(ds_dt), 3)]

print("Doanh thu cac quy:", ds_quy)

# e)
tang_truong = [
    round((ds_dt[i] - ds_dt[i-1]) / ds_dt[i-1] * 100, 2)
    for i in range(1, len(ds_dt))
]

print("Toc do tang truong (%):")

for i in range(len(tang_truong)):
    print("Thang", i + 1, "-> Thang", i + 2, ":", tang_truong[i], "%")