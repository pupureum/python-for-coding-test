'''
    Date : 2022년 9월 27일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 성적이 낮은 순서로 학생 출력하기
'''

n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# lambda로 key를 이용하여 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
