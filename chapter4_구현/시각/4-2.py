n = int(input())
count = 0

for i in range(n + 1):
    for k in range(60):
        for j in range(60):
            # 문자열들을 합쳐서 그 안에 3이 포함되어 있는지 확인
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)