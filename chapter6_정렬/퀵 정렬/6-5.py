'''
    Date : 2022년 9월 27일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 파이써닉 퀵 정렬 예제
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 가지고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
