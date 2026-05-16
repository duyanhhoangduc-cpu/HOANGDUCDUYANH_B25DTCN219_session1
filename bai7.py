a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

if a + b > c and a + c > b and b + c > a:
    print("La 3 canh tam giac")
else:
    print("Khong phai 3 canh tam giac")