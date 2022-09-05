// 처음에 직관적으로 푼 방법
// 숫자 커졌을때도 빠르게 동작할 수 있는 방법은 파이썬 코드로 있다.

#include <iostream>
using namespace std;

int main(void)
{
	int n, k;
	int count = 0;
	cin >> n >> k;

	while(n > 1)
	{
		if (n % k == 0)
			n /= k;
		else
			n -= 1;
		count += 1;
	}

	cout << count << "\n";
}