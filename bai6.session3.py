n = int(input())

if n < 0:
    print("Số lượng phần tử không được nhỏ hơn 0")
elif n == 0:
    print("Mảng không có phần tử nào")
else:
    arr = list(map(int, input().split()))
    arr = sorted(set(arr))
    print(arr[-2])