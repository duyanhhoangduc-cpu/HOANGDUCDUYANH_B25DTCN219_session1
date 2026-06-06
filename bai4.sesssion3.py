arr = input().split()

result = [x for x in arr if x.isdigit()]

if result:
    print(*result)
else:
    print("Không có ký tự số")