s = input().lower()
aa =["a","e","i","o","u"]

vowels = any(x in s for x in aa)

if vowels:
    print("Yes")
else:
    print("No")
