'''
    Date : 2022년 9월 11일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 큐 예제
'''
from collections import deque

# deque는 스택과 큐의 장점을 모두 채택한 것으로 데이터를 넣고 빼는 속도가 리스트에 비해 효율적이며,
# queue 라이브러리를 이용하는 것보다 더 간단하다.

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
queue.append(5)
queue.append(6)
queue.popleft()

print(queue)
queue.reverse()
print(queue)