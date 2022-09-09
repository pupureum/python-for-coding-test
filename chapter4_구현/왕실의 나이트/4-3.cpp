/*
    Date : 2022년 9월 9일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 왕실의 나이트 문제
*/

#include <iostream>
using namespace std;

int dx[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[8] = {1, -1, 2, -2, 2, -2, 1, -1};
string input;

int main(void)
{
    cin >> input;
    int inputX = input[0] - 'a' + 1;
    int inputY = input[1] - '0';
    int cnt = 0;
    for (char i = 0; i < 8; i++)
    {
        int newX = inputX + dx[i];
        int newY = inputY + dy[i];
        if (newX < 1 || newY < 1 || newX > 8 || newY > 8)
            continue;
        else cnt++;
    }
    cout << cnt << '\n';
    return 0;
}
