#include <iostream>

int main(void){
	int n = 1260;
	int count = 0;
	int coinTypes[4] = {500, 100, 50, 10};

	for(int i = 0; i < 4; i++)
	{
		count += n / coinTypes[i];
		n %= coinTypes[i];
	}
	std::cout << count << std::endl;
}