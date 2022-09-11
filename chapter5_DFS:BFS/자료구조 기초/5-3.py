'''
    Date : 2022년 9월 11일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 재귀 함수 예제
'''

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# 자기 자신을 계속해서 불러오기 때문에, 어느 정도 출력하다가 오류 메세지 출력