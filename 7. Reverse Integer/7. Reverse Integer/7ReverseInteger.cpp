// 7ReverseInteger.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
using namespace std;

int reverse(int x)
{
	bool flag = false;
	if (x < 0) 
		flag = true;
	x = abs(x);
	int ans = 0;
	while (x > 0)
	{
		ans = ans * 10 + x % 10;
		x=x/10;
	}
	if (ans > 2147483647)
		return 0;
	if (flag == true)
		return -1 * ans;
	return ans;

	

}
int main()
{
	int a;
	cin >> a;
	cout << reverse(a);
	system("pause");
    return 0;
}

