n = int(input())

numbers = list(map(int, input().split()))


if all(num >= 0 for num in numbers):
    print("Yes")
else:
    print("No")
