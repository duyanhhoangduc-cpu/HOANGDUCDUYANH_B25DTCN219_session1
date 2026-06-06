n = int(input())

if n == 0:
    print("Mảng không có phần tử")
else:
    arr = input().split()

    nums = [int(x) for x in arr if x.lstrip('-').isdigit()]

    if nums:
        print(sum(nums))
    else:
        print("Không có phần tử nào là số")