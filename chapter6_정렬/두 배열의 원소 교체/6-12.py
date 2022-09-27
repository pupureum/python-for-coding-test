'''
    Date : 2022년 9월 27일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 두 배열의 원소 교체
'''

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))