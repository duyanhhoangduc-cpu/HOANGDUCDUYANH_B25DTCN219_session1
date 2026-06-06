arr = list(map(int, input().split()))

if not arr:
    print("Không có số lớn nhất")
else:
    max_value = max(arr)
    print("Số lớn nhất:", max_value)
    print("Vị trí:", arr.index(max_value))