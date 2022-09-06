#include <iostream>
using namespace std;

int n;
string plans;
int x = 1, y = 1;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char move_types[4] = {'L', 'R', 'U', 'D'};

int main(void)
{
	cin >> n;
	cin.ignore(); // 남겨진 '\n'을 getline은 가져오기 때문에
				  // 버퍼를 비워줘야 한다.
	getline(cin, plans);

	for(int i = 0; i < plans.size(); i++)
	{
		char plan = plans[i];
		int nx = -1, ny = -1;
		for (int j = 0; j < 4; j++)
		{
			if (plan == move_types[j])
			{
				nx = x + dx[j];
				ny = y + dy[j];
			}
		}
		if (nx < 1 || ny < 1 || nx > n || ny > n)
			continue;
		x = nx;
		y = ny;
	}
	cout << x << ' ' << y << "\n";
	return 0;
}