'''
    Date : 2022년 9월 17일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 선택 정렬 예제
'''

array = [7, 4, 8, 0, 3, 9, 1, 6, 5, 2]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)