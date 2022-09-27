'''
    Date : 2022년 9월 27일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 위에서 아래로
'''

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse = True)
for i in array:
    print(i, end = ' ')