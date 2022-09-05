#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int n, m, k;
	int result = 0;
	vector<int> vec;

	cin >> n >> m >> k;
	for(int i = 0; i < n; i++)
	{
		int x;
		cin >> x;
		vec.push_back(x);
	}

	sort(vec.begin(), vec.end());
	int first = vec[n - 1];
	int second = vec[n - 2];

	while(true)
	{
		for(int i = 0; i < k; i++)
		{
			if (m == 0)
				break;
			result += first;
			m -= 1;
		}
		if (m == 0)
			break;
		result += second;
		m -= 1;
	}
	cout << result << endl;
}