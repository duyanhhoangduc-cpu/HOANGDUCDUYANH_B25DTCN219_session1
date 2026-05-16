so = int(input("Nhap mot so nguyen: "))

if so % 3 == 0 and so % 5 == 0:
    print("So vua nhap chia het cho ca 3 va 5")
elif so % 3 == 0:
    print("So vua nhap chia het cho 3")
elif so % 5 == 0:
    print("So vua nhap chia het cho 5")
else:
    print("So vua nhap khong chia het cho 3 va 5")