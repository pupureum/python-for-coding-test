#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
	int n, m, result = -1;
	cin >> n >> m;

	for(int i = 0; i < n; i++)
	{
		int max_value = 10001;
		for (int j = 0; j < m; j++)
		{
			int x;
			cin >> x;
			/* if (x < max_value)
				max_value = x;
				위 코드를 아래 방법과 같이 min, max_value 함수로 코드 수를 줄일 수 있다! */
			max_value = min(max_value, x);
		}
		/* if (result < max_value)
			result = max_value; */
			result = max(result, max_value);
	}

	cout << result << '\n';
}