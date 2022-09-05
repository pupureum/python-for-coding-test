n, k = map(int, input().split())
count = 0

while True:
    # 미리 나눠질 수 있는 타켓 숫자를 구해서 한꺼번에 빼놓기
    target = (n // k) * k
    count += (n - target)
    if n < k:
        break
    n = target
    
    count += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)
print(count)