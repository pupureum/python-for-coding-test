'''
    Date : 2022년 9월 11일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 재귀 함수 종료 예제
'''

def recursive_function(i):
    if i == 100:
        return
    print(i, '번쩨 재귀 함수에서', i + 1, '번쩨 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번쩨 재귀 함수를 종료합니다.')

recursive_function(1)

# 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다.
