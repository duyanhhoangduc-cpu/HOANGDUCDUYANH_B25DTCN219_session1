n = int(input("Nhap so nguyen duong n: "))

so_goc = n
so_dao = 0

while n > 0:
    chu_so = n % 10
    so_dao = so_dao * 10 + chu_so
    n = n // 10

if so_goc == so_dao:
    print("Day la so doi xung")
else:
    print("Day khong phai la so doi xung")