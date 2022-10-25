'''
    Date : 2022년 10월 26일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 부품 찾기
'''

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
target = list(map(int, input().split()))

for i in target:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')