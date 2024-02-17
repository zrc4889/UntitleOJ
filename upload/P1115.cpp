#include <bits/stdc++.h>
using namespace std;

int n, ans;

int main()
{
	cin >> n;
	
	vector<int> a(n + 1), dp(n + 1);
	
	for (int i(1); i <= n; ++ i)
		cin >> a[i];
	
	for (int i(1); i <= n; ++ i)
	{
		dp[i] = max(dp[i - 1] + a[i], a[i]);
		ans = max(ans, dp[i]);
	}
	
	cout << ans << '\n';
	return 0;
}