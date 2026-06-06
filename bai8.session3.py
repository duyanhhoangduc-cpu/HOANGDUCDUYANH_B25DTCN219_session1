arr = []


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    print("\n================== MENU ===================")
    print("1. Nhập số phần tử cần nhập và giá trị các phần tử")
    print("2. In ra giá trị các phần tử đang quản lý")
    print("3. In ra giá trị các phần tử chẵn và tính tổng")
    print("4. In ra giá trị lớn nhất và nhỏ nhất trong mảng")
    print("5. In ra các phần tử là số nguyên tố trong mảng và tính tổng")
    print("6. Nhập vào một số và thống kê trong mảng có bao nhiêu phần tử đó")
    print("7. Thêm một phần tử vào vị trí chỉ định")
    print("8. Thoát")
    print("============================================")

    choice = int(input("Lựa chọn của bạn: "))

    if choice == 1:
        n = int(input("Nhập số phần tử: "))
        arr = []
        for i in range(n):
            arr.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

    elif choice == 2:
        if len(arr) == 0:
            print("Mảng rỗng")
        else:
            print("Các phần tử:", *arr)

    elif choice == 3:
        even_nums = [x for x in arr if x % 2 == 0]
        if len(even_nums) == 0:
            print("Không có số chẵn")
        else:
            print("Các số chẵn:", *even_nums)
            print("Tổng:", sum(even_nums))

    elif choice == 4:
        if len(arr) == 0:
            print("Mảng rỗng")
        else:
            print("Giá trị lớn nhất:", max(arr))
            print("Giá trị nhỏ nhất:", min(arr))

    elif choice == 5:
        prime_nums = [x for x in arr if is_prime(x)]
        if len(prime_nums) == 0:
            print("Không có số nguyên tố")
        else:
            print("Các số nguyên tố:", *prime_nums)
            print("Tổng:", sum(prime_nums))

    elif choice == 6:
        x = int(input("Nhập số cần thống kê: "))
        print("Số lần xuất hiện:", arr.count(x))

    elif choice == 7:
        value = int(input("Nhập giá trị cần thêm: "))
        pos = int(input("Nhập vị trí cần thêm: "))

        if 0 <= pos <= len(arr):
            arr.insert(pos, value)
            print("Mảng sau khi thêm:", *arr)
        else:
            print("Vị trí không hợp lệ")

    elif choice == 8:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")