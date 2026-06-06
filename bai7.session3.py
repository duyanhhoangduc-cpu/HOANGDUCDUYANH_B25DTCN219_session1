n = int(input())

if n == 0:
    print("Không phải dãy số fibonacci")
else:
    arr = list(map(int, input().split()))

    check = True

    for i in range(2, n):
        if arr[i] != arr[i - 1] + arr[i - 2]:
            check = False
            break

    if check:
        print("Là dãy số fibonacci")
    else:
        print("Không phải dãy số fibonacci")