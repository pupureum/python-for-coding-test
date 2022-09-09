'''
    Date : 2022년 9월 9일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 왕실의 나이트 문제
'''

input = input()
inputX = int(ord(input[0])) - int(ord('a')) + 1
inputY = int(input[1])

steps = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

cnt = 0
for step in steps:
    newX = inputX + step[0]
    newY = inputY + step[1]
    if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
        cnt += 1

print(cnt)