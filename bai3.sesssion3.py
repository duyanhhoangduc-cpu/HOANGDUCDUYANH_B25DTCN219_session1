arr = list(map(int, input().split()))

if len(arr) == 0:
    print("Không có số lớn nhất")
else:
    print("Số lớn nhất:", max(arr))
    print("Vị trí:", arr.index(max(arr)))