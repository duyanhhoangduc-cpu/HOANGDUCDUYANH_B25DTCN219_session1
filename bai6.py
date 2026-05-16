a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))

print("Cac so nguyen to trong khoang [a, b] la:")

for n in range(a, b + 1):
    if n > 1:
        la_so_nguyen_to = True

        for i in range(2, n):
            if n % i == 0:
                la_so_nguyen_to = False
                break

        if la_so_nguyen_to:
            print(n)