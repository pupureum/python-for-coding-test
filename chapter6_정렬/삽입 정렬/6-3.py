'''
    Date : 2022년 9월 26일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 삽입 정렬 예제
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 -1씩 감소하며 반복
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)