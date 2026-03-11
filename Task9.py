n = int(input())
keys = input().split()
values = input().split()


query_key = input()

my_dict = dict(zip(keys, values))

result = my_dict.get(query_key, "Not found")

print(result)
