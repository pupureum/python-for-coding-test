# 3-2 풀이는 m의 크기가 100억 이상으로 커진다면 시간 초과 된다.
# 아래 방법은 수학적 아이디어를 이용해 효율적으로 풀이한 방법이다.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)