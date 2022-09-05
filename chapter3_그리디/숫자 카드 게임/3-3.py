n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    max_value = min(data)
    result = max(result, max_value)

print(result)