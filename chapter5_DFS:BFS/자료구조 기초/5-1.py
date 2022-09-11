'''
    Date : 2022년 9월 11일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 스택 예제
'''

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.pop()
stack.append(5)
stack.append(6)
stack.pop()

print(stack)
print(stack[::-1]) # 최상단 원소부터 출력