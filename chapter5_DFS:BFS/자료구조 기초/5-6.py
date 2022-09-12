'''
    Date : 2022년 9월 11일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 인접 행렬 방식 예제
'''

INF = 999999999 # 무한의 비용(연결 되어 있지 않은 노드 끼리) 선언

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)