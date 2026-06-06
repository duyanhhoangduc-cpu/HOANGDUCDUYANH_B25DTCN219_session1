arr = list(map(int, input().split()))

result = [x for x in arr if x >= 10]

if result:
    print(*result)
else:
    print("Không có số nào lớn hơn 10")