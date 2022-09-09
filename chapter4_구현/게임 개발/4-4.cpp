/*
    Date : 2022년 9월 9일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 게임 개발 문제
*/

#include <iostream>
using namespace std;

int n, m, x, y, direction;
int d[50][50];
int arr[50][50];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

void turn_left()
{
    direction -= 1;
    if (direction == -1)
        direction = 3;
}

int main(void)
{
    cin >> n >> m;
    cin >> x >> y >> direction;
    d[x][y] = 1;

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            int x;
            cin >> x;
            arr[i][j] = x;
        }
    }
    
    int cnt = 1;
    int turn_time = 0;
    while(true)
    {
        turn_left();
        int nx = x + dx[direction];
        int ny = y + dy[direction];

        if (d[nx][ny] == 0 && arr[nx][ny] == 0)
        {
            d[nx][ny] = 1;
            x = nx;
            y = ny;
            cnt += 1;
            turn_time = 0;
            continue;
        }
        else turn_time += 1;
        if (turn_time == 4)
        {
            nx = x - dx[direction];
            ny = y - dy[direction];
            if (arr[nx][ny] == 0)
            {
                x = nx;
                y = ny;
            }
            else break;
            turn_time = 0;
        }
    }
    cout << cnt << '\n';
    return 0;
}
