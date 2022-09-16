/*
    Date : 2022년 9월 16일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 미로 탈출 예제
*/

#include <iostream>
#include <queue>
using namespace std;

int n, m;
int graph[201][201];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int bfs(int x, int y)
{
    queue<pair<int, int> > q;
    q.push(pair<int,int>(x,y));

    while(!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 미로 공간 벗어나는 경우
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            // 벽인 경우 무시
            if (graph[nx][ny] == 0)
                continue;
            // 해당 노드 처음 방문인 경우에만 최단거리 기록
            if (graph[nx][ny] == 1)
            {
                graph[nx][ny] = graph[x][y] + 1;
                q.push(pair<int, int>(nx, ny));
            } 
        }
    }
    return graph[n - 1][m - 1];
}

int main(void)
{
    cin >> n >> m;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            scanf("%1d", &graph[i][j]);
        }
    }
    cout << bfs(0, 0) << "\n";
    return 0;
}